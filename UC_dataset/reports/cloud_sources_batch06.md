# 第 06 批：区域电力系统、部门耦合与 LEGO 官方算例

日期：2026-10-16，第 02 次工作。延续计划 v0.5，只收集官方原件和溯源信息；COPT 主用、Gurobi 后续兼容，尚不进行参数验证、适配或求解。

## JRC Dispa-SET EnVarClim

[Zenodo 正式记录](https://zenodo.org/records/3775569)，DOI `10.5281/zenodo.3775569`，v1，2020-04-29。发布者为 JRC 的 Matteo De Felice，关联报告 DOI `10.2760/75312`。DataCite 注册元数据明确列 CC BY 4.0，见 [保存的许可与引用记录](zenodo_datacite_metadata_batch06.json)。

正式记录提供三份配套文件：`EnVarClim-inputs-dispa-set.zip`、`EnVarClim.yml`、`README.md`。收集时三者一起归档，避免只取得时序文件而遗漏机组参数与配置。官方说明涵盖机组参数、可用率、逐时负荷、停运、跨区域传输容量/潮流、燃料和 CO2 价格、水库水位和水电入流，气候年为 1990–2015。

使用边界保留上游说明：

- 这是 Dispa-SET 区域 UC/调度模型的输入，不是节点级 IEEE SCUC。
- 配置为模板，需要在后续使用时设置路径并选择 `XXXX` 对应气候年。本轮未填写或执行。
- 官方记录指出部分西巴尔干传输行名称末尾有 `1`，不匹配模拟区域并被原模型忽略。本项目保留原文件及说明，没有静默修改。
- 部分西巴尔干时间序列在气候年之间复用，不能将所有文件描述为独立观测场景。
- CO2 价格输入不等于已经提供碳排放总量约束。独立的上游结果记录本批没有下载。

## Dispa-SET 欧洲部门耦合

[作者正式数据记录](https://zenodo.org/records/3627259)，DOI `10.5281/zenodo.3627259`，v1。作者来自 KU Leuven、Politecnico di Milano 和 European Commission。标题为 *The potential of sector coupling in future European energy systems soft linking between the Dispa-SET and JRC-EU-TIMES models - Dataset*。

记录提供一个 7z 原包，说明其包含论文配套数据及研究使用的 Dispa-SET 版本，关键词包括电动车、热储能和水电。Zenodo 与 DataCite 均明确数据许可 CC BY 4.0；包内软件保留各自原许可，不将数据许可覆盖软件。

该包保留原字节，仅在 Release 使用简短附件名。没有解压 7z、解析输入或执行软件。与 JRC EnVarClim 共用模型体系，但属于不同研究数据发布；不能计作两个独立求解器/软件库，也不能据此声称新增了独立标准测试电网。

## TU Graz LEGO

[官方仓库](https://github.com/IEE-TUGraz/LEGO)，固定提交 `eb0cb5d478305bfd97c2f2ae952c01fcf87db743`。MIT LICENSE 的版权所有者为 © 2022 IEE-TUGraz，整包保留原始 LICENSE。论文：S. Wogrin、D. Tejada-Arango、R. Gaugl、T. Klatzer、U. Bachhiesl (2022)，DOI `10.1016/j.softx.2022.101141`。见 [Git 树与许可证证据](lego_source_metadata_batch06.json)。

根目录包含 `LEGO-Base-Case-Study-1LRP.zip`、`LEGO-Base-Case-Study-7LRP.zip`、`LEGO-Base-Case-Study-Hourly.zip`，以及 `LEGO.gms`、手册和 README。官方说明明确 7LRP 为七个代表日、Hourly 为全年逐时方式；1LRP 保留官方包名，本轮不凭文件名补充参数解释。

LEGO 是包含可选 UC 的运行/扩展规划模型，支持储能、需求侧管理、氢能、惯量等模块。模型有某个功能，不代表每份默认算例都已开启该功能。三份时间表示包也不等于三个不同物理系统。

完整仓库包同时保留 `PreviousData/EnStOpInvMo-7LRP-kmeans-net.xlsm`。README 明确该旧数据与当前 `LEGO.gms` 不兼容，按历史原件保留并标记，不能当成当前版本的可运行组合。没有打开宏工作簿、解析其单元格或执行 GAMS。

## 采集与发布

[第 06 批 Release](https://github.com/djxxju/UC_datas_codex/releases/tag/official-data-2026-10-16-batch06) 已公开，对应 [云端运行](https://github.com/djxxju/UC_datas_codex/actions/runs/38844531693) 成功，工作流提交 `d504e13dfdfe6da831ad7580f1e0b39a946a5a49`。三个数据包合计 **230,107,656 字节**，另有 ATTRIBUTION、manifest、receipt，共六个附件。

| 数据包 | 发布字节数 | SHA-256 |
|---|---:|---|
| JRC-Dispa-SET-EnVarClim-inputs-v1.zip | 151,002,846 | `26e36e8a62258548516ee19690f69cefb9ef11dfdeed831f8261866d09a556ec` |
| Dispa-SET-sector-coupling-zenodo-v1.7z | 18,326,639 | `d71638e21bf27b9cdb77918dc52ddd9761f268e2923e6790b578f2a5a527355e` |
| TU-Graz-LEGO-eb0cb5d4.zip | 60,778,171 | `c4363bf5da2464f3472052cc0073d51294e5633d8042a4031b39ef5bf7dc4875` |

共下载五个原始文件，263,769,173 字节。JRC 原 ZIP 为 184,657,976 字节，连同两个小文件经过外层压缩后发布包较小，内层 ZIP 字节不变。四个 Zenodo 文件的 MD5 均与官方清单一致；LEGO 官方归档已记录下载 SHA-256。

已读取约 9 KB 的 [云端采集回执](cloud_collection_receipt_batch06.json)，核对回执本身及三个数据包的大小/SHA-256 均匹配 [GitHub 附件元数据](github_release_batch06.json)。LEGO 外层 ZIP 目录确认十四个原文件及三份预制算例 ZIP；未打开内层工作簿。7z 未解包。所有原包均未下载到本机。

本地只保存 [固定 manifest](../sources/cloud_collection_2026-10-16_batch06.json)、元数据与文档，原始大包在 GitHub 托管运行器采集。JRC 三个文件增加外层 ZIP 与说明，内部原 ZIP 不展开；其他两包不改字节。官方 MD5、采集 SHA-256、大小和时间仅用于传输身份识别，不构成参数、可行性或最优性验证。

## 本轮找到但未采集的条目

[Unit Commitment in a Federalized Power Market: A Mixed Integer Programming Approach 配套材料](https://elsevier.digitalcommonsdata.com/datasets/nr547fv6mw/1)，Payal Mitra，2022-07-12，DOI `10.17632/nr547fv6mw.1`，CC BY 4.0。正式页面说明有整理好的输入、GAMS 代码和作者结果，但文件列表在当前读取中没有取得，Mendeley 公共 API 返回 403。因此仅登记入口，未声称已下载或发布；机构字段的 Elsevier BV 是仓储发布平台，不冒充作者任职单位。

[Market-Based Power System Test Cases Data](https://data.mendeley.com/datasets/82jdrt326s/1)提供成本、容量因子与排放因子等扩展资料，本轮不把它列为完整 UC 新算例库。国内省级完整合成系统、独立需求响应或碳总量约束 UC 原包仍需继续查找。
