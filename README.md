# UC 官方现成算例库收集

当前优先收集基准项目、原作者和研究机构已经整理好的 UC 文件，保留原格式、版本、许可与引用。**按用户 2026-10-15 的最新指示，参数校验、格式转换和求解暂缓。** 以后需要本机求解时使用 COPT。

## 从这里开始

完整入口：[官方现成算例库清单](UC_dataset/官方现成算例库清单.md)。

| 来源 | 本地已取得 | 本仓库公开内容 |
|---|---|---|
| PGLIB-UC | 56 个 JSON 算例及 7 个配套文件 | 全部原件，已在上一批发布 |
| Tejada 作者 UC-data | 官方仓库整包；另取出 2 个原始 ZIP、GAMS 模型、README、LICENSE | 本批发布上述 5 个原件；实例 ZIP 和结果 ZIP 保持封装 |
| UnitCommitment.jl | OR-LIB 42、Tejada19 49、MATPOWER 代表日 26，共 117 个 `.json.gz` | 官方索引、下载脚本和采集回执 |
| 比萨大学 CommaLAB | 4 个官方现成数据包 | 官方下载链接、说明、获取脚本和采集回执 |
| RTS-GMLC v0.2.3 | 官方整包 84,452,206 字节 | 固定版本下载入口、预制格式说明和采集回执 |

Tejada 原件：[作者包目录](UC_dataset/raw/tejada_author/1b417ece7ca61d41fca7302df6a0313f8236d611/)，其中 [UC-Instances.zip](UC_dataset/raw/tejada_author/1b417ece7ca61d41fca7302df6a0313f8236d611/UC-Instances.zip) 是实例包，[UC-Instances-ResultsSummary.zip](UC_dataset/raw/tejada_author/1b417ece7ca61d41fca7302df6a0313f8236d611/UC-Instances-ResultsSummary.zip) 是作者发布的结果汇总。后者仅标为上游参考结果，没有在本项目复现或重新判定最优性。

UC.jl 外部实例及 CommaLAB 包的独立再分发条款尚未明确，原件保留本地，仓库提供官方获取方式。RTS 大包保留本地，使用官方固定版本入口获取，避免在 Git 历史重复存放大文件。许可与引用见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## 仅采集原文件

从仓库根目录运行以下命令；下载脚本只记录来源、字节数和 SHA-256，不检查 UC 参数、不建模、不求解。

```powershell
python UC_dataset/sources/collect_ucjl.py --family or-lib --family tejada19 --family matpower --no-proxy
python UC_dataset/sources/collect_official_packages.py commalab_rcuc commalab_rcuc2 commalab_118 commalab_brazil --no-proxy
python UC_dataset/sources/collect_official_packages.py rts_gmlc_v023 tejada_author
```

`--no-proxy` 只影响当前进程；按网络环境选择是否使用。本机此次对 UC.jl/CommaLAB 使用直连，对 GitHub 归档使用现有代理。未修改系统网络设置。

MATPOWER 的 26 个条目是每个系统一个代表日，不是全年文件已收齐。UC.jl 的 56 个 PGLIB 转换条目与原库同源，本轮没有重复采集；Tejada 原始版与 UC.jl 转换版也不叠加为独立系统。

## 已归档的 PGLIB-UC

固定提交 `39a7f38cf4703de92f0291f0c873c2e98c789301`；全部为 48 小时、1 小时时间步长，无网络约束。CA 20 个、FERC 24 个、RTS-GMLC 派生 12 个。

- [PGLIB 原始数据、模型及参考程序](UC_dataset/raw/pglib_uc/39a7f38cf4703de92f0291f0c873c2e98c789301/)
- [56 例索引](UC_dataset/catalog.json)
- [上一轮基础检查记录](UC_dataset/reports/pglib_integrity.json)：属于用户要求暂缓验证之前的历史工作，本轮未重跑。

数据采用 CC BY 4.0，参考程序采用 MIT，原始许可与引用保留。上游参考模型依赖相应建模环境，当前没有完成本机 COPT UC 适配；也不宣称已经可直接输入 Gurobi、CPLEX 或 UnitCommitment.jl。

## 项目管理

每次开始前阅读[项目计划书](项目计划书.md)、[项目进度](项目进度.md)和最新[工作日志](工作日志/)；结束时追加总结并更新进度。固定约定见 [AGENTS.md](AGENTS.md)。当前计划 v0.3：先收集官方现成库，再安排后续规范与求解工作。
