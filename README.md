# UC 官方现成算例库

先收集基准项目、原作者和研究机构已经整理好的 UC 文件，保留原格式、版本、许可与引用。**GitHub 是主要保存位置；参数校验、格式转换和求解暂缓。** 当前本机主求解器为 COPT，Gurobi 为用户明确的后续兼容目标，尚未完成适配。

## 获取数据

第一次访问可直接看 [算例访问指南](UC_dataset/访问指南.md)：列出全部已镜像来源、直接下载地址，以及仅提供官方入口的来源。

**完整原包请到 [GitHub Releases](https://github.com/djxxju/UC_datas_codex/releases) 下载。** [第 07 批](https://github.com/djxxju/UC_datas_codex/releases/tag/official-data-2026-10-17-batch07)新增 openSDUC 与 OPTIT 冷热电联供测试材料；[第 06 批](https://github.com/djxxju/UC_datas_codex/releases/tag/official-data-2026-10-16-batch06)保存 JRC 区域输入、欧洲部门耦合和 LEGO；[第 05 批](https://github.com/djxxju/UC_datas_codex/releases/tag/official-data-2026-10-16-batch05)保存 HUST 水电 UC 与 RPG Lab SCUC；[第 04 批](https://github.com/djxxju/UC_datas_codex/releases/tag/official-data-2026-10-15-batch04)保存 RTS、Tejada、随机 UC 和 Monash 包。均由 GitHub 云端直接采集，用户电脑无需先下载再上传。

| 来源 | 已归档范围 | 主要保存位置 |
|---|---|---|
| PGLIB-UC | 56 个 UC JSON + 7 个配套文件 | [本仓库原件目录](UC_dataset/raw/pglib_uc/39a7f38cf4703de92f0291f0c873c2e98c789301/) |
| Tejada 作者 UC-data | 官方完整仓库包；包含实例、作者结果、GAMS、工作簿和 MIT 许可 | Releases 完整包；[仓库中另有 5 个核心原件](UC_dataset/raw/tejada_author/1b417ece7ca61d41fca7302df6a0313f8236d611/) |
| RTS-GMLC v0.2.3 | 完整官方 ZIP，84.5 MB，含预制工具格式及原始时序 | Releases |
| Stochastic UC data files | 新增：7 个高比例光伏随机 UC 的 JSON/HDF5 原文件 | Releases，CC BY 4.0 |
| Monash 扩展规划 UC | 新增：6 个包含 UC、网络及储能规划参数的原始工作簿 | Releases，CC BY 4.0 |
| 华中科技大学水电 UC | 新增：官方补充材料含 mmc2.xlsx，九组 15 分钟水电 UC 的作者数据及结果 | 第 05 批 Releases，CC BY 4.0，原包约 1 MB |
| 休斯顿大学 RPG Lab SCUC | 新增：Figshare V2 完整研究包，IEEE24/73/118 和合成 500 节点；含图样本和作者结果 | 第 05 批 Releases，CC BY 4.0，原包约 1.15 GB |
| JRC Dispa-SET EnVarClim | 新增：区域 UC/调度输入、配置模板与 README；涵盖气候年、机组、水库、CO2 价格等 | 第 06 批 Releases，CC BY 4.0，外层包约 151 MB |
| Dispa-SET 欧洲部门耦合 | 新增：作者研究数据与配套模型版本，原始 7z | 第 06 批 Releases，数据 CC BY 4.0，约 18.3 MB |
| TU Graz LEGO | 新增：官方完整仓库包，含 1LRP/7LRP/Hourly 三份预制包、GAMS、手册和 MIT 许可 | 第 06 批 Releases，约 60.8 MB |
| Comillas IIT openSDUC | 官方 16 机组示例、17 个 CSV 输入/字典文件、Python/Pyomo 模型与文档 | 第 07 批 Releases，AGPLv3 原许可，约 0.44 MB |
| OPTIT / 博洛尼亚 CHP–CHCP | 作者设备描述与 2022 年逐日输入两个原 ZIP 配对归档；365 日为作者说明 | 第 07 批 Releases，CC BY 4.0，约 0.46 MB |
| UnitCommitment.jl | 已有 OR-LIB 42、Tejada19 49、MATPOWER 代表日 26，共 117 文件 | 本仓库提供索引与官方获取脚本；旧原件本地保留 |
| CommaLAB | 已有 RCUC、RCUC2、118_UC、System_46buses 四个官方原包 | 本仓库提供下载入口；旧原包本地保留 |

已有十四个来源组的原件：十二个已在 GitHub 归档，UC.jl 外部实例和 CommaLAB 的独立再分发条款尚未明确，当前保留旧本地原件及官方入口。另有 REAL Lab、CUC-data、Federalized Power Market、TAMU DemandResponse、PyPSA-stochUC 五项仅登记入口。OPTIT 两份配套记录按一个来源组统计；不同 Dispa-SET 研究包共享模型体系。来源数、文件数与日场景数均不等于独立电网数。

按用途选择材料见 [分类索引](UC_dataset/官方来源分类索引.md)。LEGO 旧版数据与当前模型不兼容，已保留原件和说明。模型支持某种功能不表示默认算例已启用；CO2 价格输入也不能等同碳排放总量约束。

- [官方现成库总清单](UC_dataset/官方现成算例库清单.md)
- [第 07 批来源、下载说明与候选缺口](UC_dataset/reports/cloud_sources_batch07.md)
- [第 06 批来源与发布说明](UC_dataset/reports/cloud_sources_batch06.md)
- [第 05 批新增来源与发布说明](UC_dataset/reports/cloud_sources_batch05.md)
- [第 04 批来源与发布说明](UC_dataset/reports/cloud_sources_batch04.md)
- [仅登记入口的候选来源](UC_dataset/reports/official_candidates_batch05.md)
- [许可与引用](THIRD_PARTY_NOTICES.md)
- [来源登记](UC_dataset/sources/source_registry.json)

## 云端采集与本地恢复

[第 07 批采集工作流](.github/workflows/collect-official-data-batch07.yml)、[第 06 批](.github/workflows/collect-official-data-batch06.yml)、[第 05 批](.github/workflows/collect-official-data-batch05.yml)与[第 04 批](.github/workflows/collect-official-data.yml)在 GitHub 托管运行器上下载官方原文件、记录来源与文件摘要并发布 Releases。四批已成功，重新触发时会跳过已发布批次；增加新数据应创建新批次标签，不覆盖现有原件。

原始文件没有做参数校验或模型求解；脚本中的传输长度检查和文件哈希仅用于识别文件与确认传输。上游结果文件只标为作者参考结果，不作为本项目复现结果。

为减少本地存储，已清理 70 个有远端副本的重复文件，约 112.3 MB。GitHub 中的原件仍保留。需要本地使用时按 [清理记录的 restore_url](UC_dataset/reports/local_cleanup_completed_batch04.json)或 Releases 恢复即可；不要把本机 raw 目录为空解释为远端数据已删除。未镜像的旧资料仍保留本地。

已有下载脚本仍可按需使用，但不会自动开展校验或求解：

```powershell
python UC_dataset/sources/collect_ucjl.py --family or-lib --family tejada19 --family matpower --no-proxy
python UC_dataset/sources/collect_official_packages.py rts_gmlc_v023 tejada_author
```

PGLIB 的[上一轮基础检查记录](UC_dataset/reports/pglib_integrity.json)作为历史证据保留，本轮没有重跑。当前未完成 COPT UC 适配，也不宣称全部格式已可直接输入 Gurobi、CPLEX 或 UnitCommitment.jl。

## 项目管理

每次开始前阅读[计划书](项目计划书.md)、[项目进度](项目进度.md)和最新[工作日志](工作日志/)；结束时追加总结并更新进度。约定见 [AGENTS.md](AGENTS.md)。当前计划 v0.5：官方现成库优先、GitHub 主要保存、COPT 主用与 Gurobi 后续兼容、验证与求解暂缓。
