# RTS-GMLC 官方成套数据包入口

登记日期：2026-10-15。此次只整理官方发布包、已生成的工具格式和引用，不检查参数、不转换数据、不运行模型或求解器。以下“现成”指上游仓库已提供文件，不代表本机已验证兼容性。

## 推荐获取的官方包

首选 [RTS-GMLC v0.2.3 官方 release](https://github.com/GridMod/RTS-GMLC/releases/tag/v0.2.3)。发布于 2025-10-23，对应提交 `3ece0d3725c844056132393ee252b3083dd4eab4`，与本项目此前固定的版本一致。

- [官方 ZIP 整包](https://api.github.com/repos/GridMod/RTS-GMLC/zipball/v0.2.3)
- [官方 TAR.GZ 整包](https://api.github.com/repos/GridMod/RTS-GMLC/tarball/v0.2.3)
- [按提交固定的 ZIP 地址](https://github.com/GridMod/RTS-GMLC/archive/3ece0d3725c844056132393ee252b3083dd4eab4.zip)
- [固定版本浏览入口](https://github.com/GridMod/RTS-GMLC/tree/3ece0d3725c844056132393ee252b3083dd4eab4)

[Release API](https://api.github.com/repos/GridMod/RTS-GMLC/releases/tags/v0.2.3) 的 `assets` 为空，以上是官方仓库归档入口，不是另有独立发行附件。本轮实际下载的固定提交 ZIP 为 84,452,206 字节（约 84.5 MB）。官方 [Git tree 元数据](https://api.github.com/repos/GridMod/RTS-GMLC/git/trees/3ece0d3725c844056132393ee252b3083dd4eab4?recursive=1) 列出 209 个普通文件，文件大小合计 218,401,636 字节（约 218.4 MB，未压缩、不含子模块内容）；后者只是上游目录元数据统计，本轮没有解压确认内容。

若以后需要论文原始版本，可另收 [0.2 release](https://github.com/GridMod/RTS-GMLC/releases/tag/0.2)。上游明确该版对应论文 *The IEEE Reliability Test System: A Proposed 2019 Update*，DOI：[10.1109/TPWRS.2019.2925557](https://doi.org/10.1109/TPWRS.2019.2925557)。不把 0.2 和 v0.2.3 当成同一快照。

## 已经整理好的工具格式

以下路径均相对于同一版本仓库根目录。整包同时保留 `SourceData`、`timeseries_data_files` 和说明文件，便于维持上游相对路径。

| 官方目录 | 已提交的文件 | 当前收集定位 |
|---|---|---|
| [Prescient](https://github.com/GridMod/RTS-GMLC/tree/3ece0d3725c844056132393ee252b3083dd4eab4/RTS_Data/FormattedData/Prescient) | `rts_gmlc.dat`、`topysp.py`、`pyomosolprint.py`、README | 已有 Prescient/Pyomo 模板文件；README 说明脚本还生成 `sources.txt`，带网络版本需相应选项。因此保存整个官方包，不把单个 `.dat` 宣称为本机可直接求解的全部输入。 |
| [PLEXOS](https://github.com/GridMod/RTS-GMLC/tree/3ece0d3725c844056132393ee252b3083dd4eab4/RTS_Data/FormattedData/PLEXOS) | `RTS-GMLC.xml`、`rts_PLEXOS.xlsx`、创建脚本与 `PLEXOS_Solution` | 已整理成 PLEXOS 数据库格式；README 记录导入步骤及单位系统设置。属于官方现成工具包。 |
| [openTEPES](https://github.com/GridMod/RTS-GMLC/tree/3ece0d3725c844056132393ee252b3083dd4eab4/RTS_Data/FormattedData/openTEPES) | `RTS-GMLC/` 内已生成的 `oT_Data_*.csv`、`oT_Dict_*.csv` 等，以及生成脚本 | 已提供工具格式的 CSV 输入集合；按其 README 使用 openTEPES，暂不转换为本项目 schema。 |
| [SIIP](https://github.com/GridMod/RTS-GMLC/tree/3ece0d3725c844056132393ee252b3083dd4eab4/RTS_Data/FormattedData/SIIP) | `generator_mapping.yaml`、`user_descriptors.yaml`、`timeseries_pointers.json` | 是 PowerSystems.jl 的映射和时序指针材料，需与原始数据一起保存；不作为独立完整 UC JSON 算例包计数。 |

`PLEXOS_Solution` 中已有上游 CSV 调度、成本、潮流、发电、价格以及 HTML 报告；目前仅登记为“上游参考结果”，未复现、未评定最优性。

MATPOWER、PowerWorld、PSS/E 等目录也存在，但本轮不因其含电网模型就将其单独归为完整 UC 算例。各工具格式是 RTS-GMLC 的不同表示，不重复统计为不同基础系统。

## 许可与保留事项

许可依据为固定版本根 [README 的 DATA USE DISCLAIMER AGREEMENT](https://github.com/GridMod/RTS-GMLC/blob/3ece0d3725c844056132393ee252b3083dd4eab4/README.md)。上游允许使用、复制、分发数据，要求保留完整通知，并在使用数据的成果中致谢 DOE/NREL/ALLIANCE。记录为上游自定义数据使用条款，归档时保留 README 全文。

[`.gitmodules`](https://github.com/GridMod/RTS-GMLC/blob/3ece0d3725c844056132393ee252b3083dd4eab4/.gitmodules) 登记了 PLEXOS 创建/报告流程的 PIDG、MAGMA 子模块。GitHub 仓库归档不会把这些外部仓库内容打包进来；本次以收集已经生成的数据为目的，不执行这些生成或报告流程。

## 本轮实际状态

已获取官方 release、文件清单和说明证据，并从官方 codeload 入口下载固定版本 ZIP。使用现有系统代理的单次尝试成功；未更改代理设置或关闭 TLS 验证。原包存于 `UC_dataset/raw/official_packages/rts_gmlc/RTS-GMLC-3ece0d3725c844056132393ee252b3083dd4eab4.zip`，SHA256 为 `eb1086cc0f12f92c1a5de3f431784b324eb5bfdfdb8d8223f4c6e301bd15673e`，详见 [下载回执](official_package_collection_20261015T110456827608Z.json)。

原包只保存在本地，发布清单与官方入口；未解压、未检查内容和参数、未求解、未转换。此次新增的哈希仅用于记录下载文件身份，不构成 UC 数据或模型验证。本地原有 `raw/rts_gmlc/` 仍是此前部分材料，应与本次 ZIP 归档分别记录。
