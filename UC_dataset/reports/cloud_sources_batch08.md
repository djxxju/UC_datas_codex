# 第 08 批官方来源采集与发布

日期：2026-10-18。用户在目标格式评估后要求继续收集；本轮仅进行官方原件采集、溯源和 GitHub 归档。

## 发布结果

[第 08 批 Release](https://github.com/djxxju/UC_datas_codex/releases/tag/official-data-2026-10-18-batch08) 已公开。[云端运行 39092175293](https://github.com/djxxju/UC_datas_codex/actions/runs/39092175293)成功，采集提交 `e531876941a551236bb3dcb9512675fe2c564ba7`。两个原始数据包共 **168,120,201 字节**，另附 ATTRIBUTION.md、source_manifest.json 和 collection_receipt.json，共五个附件。

| 来源 | 固定提交 | 数据包 | 大小 |
|---|---|---|---:|
| Comillas IIT openTEPES | `5c0187063874cca4bc7af8ff97b19c6c316dd7a5` | [直接下载](https://github.com/djxxju/UC_datas_codex/releases/download/official-data-2026-10-18-batch08/Comillas-openTEPES-5c018706.zip) | 160,837,073 字节 |
| GenX 官方示例 | `3d9596ad9ce69e66ed0404754e58250059bf612b` | [直接下载](https://github.com/djxxju/UC_datas_codex/releases/download/official-data-2026-10-18-batch08/GenX-official-examples-3d9596ad.zip) | 7,283,128 字节 |

两包均是固定提交的官方仓库 ZIP，原始内容不改。GitHub 云端下载并上传，用户电脑没有新增原包。本机只保存来源元数据、文档和 61,725 字节采集回执。

## openTEPES 的范围与入口

[官方固定版本](https://github.com/IIT-EnergySystemModels/openTEPES/tree/5c0187063874cca4bc7af8ff97b19c6c316dd7a5)由 Universidad Pontificia Comillas 的 IIT 开发。完整源码包保留 AGPLv3 LICENSE、README、模型、输入和文档。

`openTEPES/cases/` 下共有 **17 个直接子目录、737 个文件**：

`9n`、`9n7y`、`9nH2`、`9nH2x`、`9n_AC`、`9n_ELZ`、`9n_PTDF`、`9n_duckdb`、`9n_heat`、`NG2030`、`RTS-GMLC`、`RTS-GMLC_6y`、`RTS-GMLC_AC`、`RTS-GMLC_AC_Oper`、`RTS-GMLC_Oper`、`RTS24`、`sSEP`。

这是目录统计，包含同系统变体和不同存储表示；`9n_duckdb` 是另一种输入存储方式，不另计物理系统。RTS 系列与已归档 RTS-GMLC/PGLIB 具有系统层面的重叠，保留 openTEPES 专用输入，但不以此增加独立电网数量。

按官方 README，模型包含网络约束 UC、运行备用、储能、需求灵活性、多能耦合和最大 CO2 排放等功能。仅看到文件名 `oT_Data_Emission_*.csv` 不能确认每个默认例均启用了有限排放上限；本轮没有读取 CSV 参数或开关。网络约束也不自动代表通过 N-1 安全校验。

另有 `case_studies/Optimal-Power-Grid-Design` 和 `case_studies/TSO-DSO_coordination` 两类论文配套目录。官方说明它们与随包小例不同，不在上游 CI 中。配套论文 DOI 分别为 10.1016/j.segan.2024.101413、10.1016/j.epsr.2022.108480。模型主引用为 Ramos、Quispe、Lumbreras (2022)，SoftwareX，DOI 10.1016/j.softx.2022.101070；该 DOI 是模型论文而非本次数据快照 DOI。

解压后先读根 README、LICENSE、`doc/md/InputData.md`，再进入 `openTEPES/cases/9n` 或 `sSEP` 查看官方小例。保留整套模型和文档。

## GenX 的范围与入口

[官方固定版本](https://github.com/GenXProject/GenX.jl/tree/3d9596ad9ce69e66ed0404754e58250059bf612b)由 MIT、Princeton ZERO Lab 等团队维护，完整源码使用 GPLv2。旧仓库地址 GenXProject/GenX 已重定向到 GenXProject/GenX.jl，本批固定后者提交。

`example_systems/` 下 **11 个目录、240 个文件**，包括三分区基础例、电解制氢、CO2 捕集、政策松弛、分段燃料、多阶段规划、风光储共址、风光储氢共址、机组改造、IEEE 9 节点 DC OPF 和 Allam cycle/LOX 示例。归为**含 UC 机制的扩展规划配套数据**，不能笼统称为 11 个整数 UC 基准。

官方示例 README 已披露的重要差异：

- `3_three_zones_w_co2_capture` 采用线性聚合 UC（UCommit=2）。同文将碳约束称为 mass-based，却使用 gCO2/kWh 单位；保留上游描述冲突，后续转换前须核实，不自行修正。
- `4_three_zones_w_policies_slack` 允许政策约束以罚成本形式松弛，包括碳政策；不能作为本项目已经验证的硬碳总量约束基准。
- `10_IEEE_9_bus_DC_OPF` 明确是 DC OPF 演示，不据此断言启用了 UC。
- `1_three_zones` 说明年度逐小时的三个新英格兰分区，含火电、风光及储能，提供碳约束文件；具体设置是否生效未核查。

解压后先读根 README 和 LICENSE，再读目标 `example_systems/<name>/README.md`，配套 resources、system、policies 和 settings 一并保留。上游 Run.jl 是作者运行入口，本项目未运行或适配 COPT/Gurobi。软件概念 DOI 10.5281/zenodo.10846069 不替代本批固定提交标识。

## 本次实际核对

- 实时读取官方仓库、固定提交、完整 Git 树、LICENSE、README 和部分示例说明；未解析参数表。
- 云端只读取 ZIP 中央目录并检查预期文件名，没有解压执行上游程序。
- 回执与 GitHub 附件的大小和 SHA-256 一致；回执下载本身的 SHA-256 也与 GitHub 记录一致。
- openTEPES ZIP 的 1,050 个文件/833,931,449 未压缩字节，与固定 Git 树一致；GenX 为 936 个文件/24,888,678 未压缩字节。全仓库文件包括模型、文档、测试及示例，不等于算例数。
- 没有运行参数检查、正式 Schema、转换器、COPT/Gurobi、基准计算或结果复现。

原包 SHA-256：

- openTEPES：`54c4b64f225a2912d12f8a1e7ba4ea4921d0461db527f21f475b4ed030a72113`
- GenX：`3489f684f320a7ea77cd011476c4e2c6d7929d450e260ef1d62fdaccb00b9aee`

证据：[固定源元数据](official_source_metadata_batch08.json)、[来源筛选记录](source_screening_batch08.json)、[云端回执](cloud_collection_receipt_batch08.json)、[发布记录](github_release_batch08.json)、[发布核对](publication_audit_batch08.json)、[采集清单](../sources/cloud_collection_2026-10-18_batch08.json)。

## 尚未收集的线索与下一步

国内省级完整合成 UC 包仍未取得。本次国家基础学科数据中心线索在检索摘要中指向光伏预测，打开网页未返回完整元数据字段，不能据此认定存在完整 UC 输入，也未取得明确再分发依据。

[FERC 官方 RTO 测试页](https://www.ferc.gov/power-sales-and-markets/increasing-efficiency-through-improved-software/rto-unit-commitment-test)明确区分公开机组/需求资料与受 CEII 限制的网络及样例模型。本轮仅记线索，不下载受限材料、不联系作者；已有 PGLIB FERC 派生 JSON 不等于原站完整网络包。

当前累计 **16 个有原件来源组、14 个有 GitHub 原件镜像、2 个旧本地来源、5 个仅入口候选**。GitHub 保存 PGLIB 原件目录和 13 个 Release 数据附件。继续采集时优先核查国内完整研究包、公开 FERC 冬夏资料的去重关系，以及需求响应研究包的明确授权；标准化按已有评估另行推进。
