# UC 官方现成算例库

先收集基准项目、原作者和研究机构已经整理好的 UC 文件，保留原格式、版本、许可与引用。**GitHub 是主要保存位置；参数校验、格式转换和求解暂缓。** 后续本机求解器使用 COPT。

## 获取数据

**大型完整包请到 [GitHub Releases](https://github.com/djxxju/UC_datas_codex/releases/tag/official-data-2026-10-15-batch04) 下载。** 本批由 GitHub 云端直接采集，用户电脑无需先下载再上传。

| 来源 | 已归档范围 | 主要保存位置 |
|---|---|---|
| PGLIB-UC | 56 个 UC JSON + 7 个配套文件 | [本仓库原件目录](UC_dataset/raw/pglib_uc/39a7f38cf4703de92f0291f0c873c2e98c789301/) |
| Tejada 作者 UC-data | 官方完整仓库包；包含实例、作者结果、GAMS、工作簿和 MIT 许可 | Releases 完整包；[仓库中另有 5 个核心原件](UC_dataset/raw/tejada_author/1b417ece7ca61d41fca7302df6a0313f8236d611/) |
| RTS-GMLC v0.2.3 | 完整官方 ZIP，84.5 MB，含预制工具格式及原始时序 | Releases |
| Stochastic UC data files | 新增：7 个高比例光伏随机 UC 的 JSON/HDF5 原文件 | Releases，CC BY 4.0 |
| Monash 扩展规划 UC | 新增：6 个包含 UC、网络及储能规划参数的原始工作簿 | Releases，CC BY 4.0 |
| UnitCommitment.jl | 已有 OR-LIB 42、Tejada19 49、MATPOWER 代表日 26，共 117 文件 | 本仓库提供索引与官方获取脚本；旧原件本地保留 |
| CommaLAB | 已有 RCUC、RCUC2、118_UC、System_46buses 四个官方原包 | 本仓库提供下载入口；旧原包本地保留 |

UC.jl 外部实例和 CommaLAB 的独立再分发条款尚未明确，当前不做公开镜像。来源有转换和派生重叠，不把文件数直接相加为独立系统数。Monash 是含 UC 的扩展规划数据，保留其原始用途与 XLSX 格式，当前未统一成 JSON。

- [官方现成库总清单](UC_dataset/官方现成算例库清单.md)
- [本批新增来源与发布说明](UC_dataset/reports/cloud_sources_batch04.md)
- [许可与引用](THIRD_PARTY_NOTICES.md)
- [来源登记](UC_dataset/sources/source_registry.json)

## 云端采集与本地恢复

[采集工作流](.github/workflows/collect-official-data.yml)在 GitHub 托管运行器上下载官方原文件、记录来源与文件摘要并发布 Releases。当前批次已经成功，重新触发时会跳过已发布批次；增加新数据应创建新批次标签，不覆盖现有原件。

原始文件没有做参数校验或模型求解；脚本中的传输长度检查和文件哈希仅用于识别文件与确认传输。上游结果文件只标为作者参考结果，不作为本项目复现结果。

为减少本地存储，已清理 70 个有远端副本的重复文件，约 112.3 MB。GitHub 中的原件仍保留。需要本地使用时按 [清理记录的 restore_url](UC_dataset/reports/local_cleanup_completed_batch04.json)或 Releases 恢复即可；不要把本机 raw 目录为空解释为远端数据已删除。未镜像的旧资料仍保留本地。

已有下载脚本仍可按需使用，但不会自动开展校验或求解：

```powershell
python UC_dataset/sources/collect_ucjl.py --family or-lib --family tejada19 --family matpower --no-proxy
python UC_dataset/sources/collect_official_packages.py rts_gmlc_v023 tejada_author
```

PGLIB 的[上一轮基础检查记录](UC_dataset/reports/pglib_integrity.json)作为历史证据保留，本轮没有重跑。当前未完成 COPT UC 适配，也不宣称全部格式已可直接输入 Gurobi、CPLEX 或 UnitCommitment.jl。

## 项目管理

每次开始前阅读[计划书](项目计划书.md)、[项目进度](项目进度.md)和最新[工作日志](工作日志/)；结束时追加总结并更新进度。约定见 [AGENTS.md](AGENTS.md)。当前计划 v0.4：官方现成库优先、GitHub 主要保存、验证与求解暂缓。
