# 第 09 批：Plan4Res 官方数据与候选补查

日期：2026-10-18。本轮继续官方现成数据采集，不开展标准化或求解。

## 已归档内容

[第 09 批 Release](https://github.com/djxxju/UC_datas_codex/releases/tag/official-data-2026-10-18-batch09)已公开，[云端运行 39113999904](https://github.com/djxxju/UC_datas_codex/actions/runs/39113999904)成功。采集提交为 `f7500213012dedeb89ddd18cadbb88f6001a7763`。

[下载 Plan4Res-EDF-CS3-v2.1-with-D4.5.zip](https://github.com/djxxju/UC_datas_codex/releases/download/official-data-2026-10-18-batch09/Plan4Res-EDF-CS3-v2.1-with-D4.5.zip)，73,237,894 字节。另有 ATTRIBUTION.md、source_manifest.json、collection_receipt.json，共四个附件。

| 原始文件 | 上游版本/记录 | 字节 | 官方 MD5 |
|---|---|---:|---|
| EDF__plan4resCS3ReferenceWithoutClimateChange__20200421__20200430__V2.1.zip | 数据 V2.1；[10.5281/zenodo.3802550](https://zenodo.org/records/3802550) | 65,893,753 | 8b681086189a440d7e7c58c6a74f6490 |
| plan4res-D4.5-Dataset_Public_v4.2.pdf | 文档 V4.2；[10.5281/zenodo.3785010](https://zenodo.org/records/3785010) | 9,251,926 | fb5be243d259ed537932b39a9065825e |

两个官方记录均明确标为开放访问、CC BY 4.0。数据作者为 EDF 的 Sandrine Charousset、Slimane Noceir、Dominique Daniel、Nadia Oudjane；文档由 Mauro Dell'Amico 等联合撰写，完整作者及机构信息保存在官方元数据快照。项目获得欧盟 Horizon 2020 项目 773897 支持。

本批将数据和配套说明合并计 **一个来源组**，不是两个系统。内部 ZIP/PDF 保留原始字节，外层只增加 SOURCE_NOTICE.md 和 SOURCE_METADATA.json。

## 覆盖范围和使用入口

正式记录将数据归类为欧洲电力系统 case study 3 的 UC、季节储能价值、灵活性及不确定性研究输入。数据文件名明确是 **ReferenceWithoutClimateChange**，因此本次只归档该固定参考情景，不能称为取得了全部气候变化情景或 Plan4Res 三个研究的全部数据。

解压外层包后先读 SOURCE_NOTICE.md、SOURCE_METADATA.json 和 D4.5 PDF，再按需展开数据 ZIP。PDF 是项目格式和数据构造说明，覆盖面不必等于本批数据范围。内层参数表、本批需求响应/碳约束具体开关、数学完整性、COPT/Gurobi 适配及基准解均未检查。没有将输入改为新的统一格式。

当前 GitHub 的 plan4res/toyDataset 是另一份版本材料；本轮检查其固定提交 `6a1db74395aa100f6cea4fa6a0190db996683660`，127 个文件未发现 README/许可证路径，不借用 Zenodo 两个记录的许可进行镜像。

## 实际核对与存储

- GitHub 云端直接获取两个官方文件，原件共 75,145,679 字节；本机没有新增数据原包或 PDF。
- 上游大小/MD5、下载 SHA-256、发布附件大小/摘要相符。最终外层 ZIP SHA-256 为 `ba17e65f5e4ee55a0bc5578d4963b6ebf9f0908afb1a33cd52c43e75afc399ce`。
- 外层 ZIP 中央目录有四个文件：两个原件与两份溯源文件；不是四个算例。内层 ZIP 未展开，PDF 正文未解析。
- 本机只保存 3,567 字节回执及来源元数据/文档；回执自身 SHA-256 与 GitHub 一致。
- 未做 UC 参数校验、格式转换、求解、原文成本复现，也未联系作者。

证据：[官方数据元数据](zenodo_3802550_batch09.json)、[官方文档元数据](zenodo_3785010_batch09.json)、[采集回执](cloud_collection_receipt_batch09.json)、[发布记录](github_release_batch09.json)、[核对记录](publication_audit_batch09.json)、[采集清单](../sources/cloud_collection_2026-10-18_batch09.json)。

## 新增的两个候选

| 候选 | 依据 | 为什么尚未镜像 |
|---|---|---|
| [DyGTCN UC 拓扑变化/需求响应](https://github.com/galigaliga/DyGTCN-for-UC-with-topology-changes/tree/197095070ee4fe6efbb838173a97b4c39a057c29) | [出版商论文页](https://www.sciencedirect.com/science/article/pii/S0378779626010047)链接该作者仓库，介绍 IEEE118、拓扑变化与可调度需求响应；固定树 50 文件 | GitHub 许可为空；完整树没有 LICENSE/COPYING/NOTICE，README 无明确再分发许可。没有执行生成器或训练程序 |
| [Closed-Loop NCUC](https://github.com/asxadf/Closed_Loop_NCUC_Dataset/tree/4c1c3c75ee8231f0d1c10ebed8926d9e15c6b1bb) | README 关联 [IEEE 2022 论文](https://ieeexplore.ieee.org/document/9617122)，提供改造 RTS24、Elia 负荷/风光、特征、MATLAB；源时序为 15 分钟，固定树 32 文件 | 没有明确许可证；公开访问及要求引用不足以确定再分发许可。未确认较大系统数据完整性 |

这两项分别是需求响应/拓扑变化和预测优化方向，不能合并称为两个完整需求响应基准。仅保存出处和目录事实，未镜像原数据。证据：[候选固定树记录](candidate_metadata_batch09.json)、[筛选记录](source_screening_batch09.json)。

## 本轮排除的误收与剩余缺口

[LIST 的需求响应条目](https://lore.list.lu/dataset.xhtml?persistentId=perma%3ALIST.6TVPVX)自述是自动抓取的文章交叉引用，Data Type 为 Article，指向 DOI 10.1109/TSG.2020.3042847；没有核实到现成输入包，不计入已采集或新增数据候选。

[FERC 官方页](https://www.ferc.gov/power-sales-and-markets/increasing-efficiency-through-improved-software/rto-unit-commitment-test)给出的公开入口已追到冬季 `20120725-4066`、夏季 `20120724-4012`，但 eLibrary 页面未返回附件行。没有下载受 CEII 限制的网络或模型；公开原始输入与现有 PGLIB FERC 派生例的去重关系仍待核实。

国内省级完整 UC 数据本轮未取得；检索未命中不证明不存在。累计 **17 个来源组有原件，15 个有 GitHub 原件，2 个为旧本地原件；另有 7 个仅入口候选**。GitHub 保存 PGLIB 原件目录和 14 个 Release 数据附件。下一轮优先推进已有来源的具体缺口，例如逐文件核查 UC.jl 原件自带许可、FERC 公开附件可达性和需求响应作者数据的公开授权；不以重复系统或论文条目增加算例数量。
