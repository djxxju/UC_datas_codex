# 第 07 批：openSDUC 与冷热电联供 UC 测试材料

日期：2026-10-17，第 02 次工作。延续计划 v0.5，收集官方现成材料、保留原格式并在 GitHub 发布。COPT 主用、Gurobi 后续兼容；参数校验、模型适配、环境测试和求解均暂缓。

## Comillas IIT openSDUC

[官方仓库](https://github.com/IIT-EnergySystemModels/openSDUC)，固定提交 `951369aad1615fc6c2281d7bd350ded393096f3a`。机构为 Universidad Pontificia Comillas 的 IIT，文档联系人 Andrés Ramos。没有确认独立数据集 DOI，因此登记为 null，不借用其他 UC 文献 DOI。

官方 Download 文档将 `openSDUC/16g` 称为 16 机组小算例。固定 Git 树有 45 个文件，其中该算例目录有 17 个 CSV 输入/字典文件；完整仓库包同时保存 Python/Pyomo 模型、README、文档与许可证。本轮只读说明及文件目录，未解析 CSV 参数。

官方模型介绍涵盖随机 UC、运行备用、需求/新能源场景、抽水蓄能和电池，可按一天或一周表示时间。该描述用于材料分类，不是对每个场景配置的独立确认。CO2 排放输出也不能据此归为碳总量约束算例。

根 `LICENSE` 为 AGPLv3，README 与下载说明一致；`pyproject.toml` 的 classifier 却写成 GPLv3+。本项目保留并披露该上游元数据差异，完整源代码和原许可证一起镜像，不修改或重新授权。证据见 [来源元数据](opensduc_metadata_batch07.json)。

下载后解压，先读根目录 README、LICENSE 和 `doc/md/InputData.md`，输入在 `openSDUC/16g`。上游列出 Gurobi 等调用方式，但本项目未安装依赖、执行模型或完成 COPT/Gurobi 适配。

## OPTIT / 博洛尼亚大学 CHP–CHCP 测试材料

两份正式记录均发布于 2024-03-26，Zenodo 和 DataCite 均注明 CC BY 4.0：

| 材料 | 作者与出处 | 上游原附件 |
|---|---|---|
| CHCP 逐日输入 | Valerio Di Felice、Luca Giuliani、Angelo Gordini；[DOI 10.5281/zenodo.10875471](https://doi.org/10.5281/zenodo.10875471) | `data.zip`，484,359 字节 |
| CHP 设备块描述 | Valerio Di Felice、Caterina Tamburini、Angelo Gordini；[DOI 10.5281/zenodo.10875998](https://doi.org/10.5281/zenodo.10875998) | `base_instance.zip`，8,678 字节 |

作者机构为 OPTIT s.r.l.；逐日输入的共同作者 Luca Giuliani 来自 University of Bologna。设备描述记录明确链接前一份输入记录，因此配对收集，合并为一个来源组。

逐日输入的作者说明为虚构但贴近实际的冷热电联供材料，包含 2022 年 365 个 JSON，字段涉及热/冷需求、购电/售电价、天然气价格。365 个逐日文件不是 365 个独立电网。单独的时序压缩包不能称作完整 UC 模型输入，需与设备描述一起使用；本轮未展开两份内层 ZIP，未确认参数完整性或时间粒度。

保留作者使用的 CHP/CHCP 名称区别，不自行补设备参数或求解模型。两份原 ZIP 放在同一外层包中，仅增加 SOURCE_NOTICE.md 和 SOURCE_METADATA.json；内部原件字节不变。

官方元数据：[逐日输入](zenodo_10875471_batch07.json)、[设备描述](zenodo_10875998_batch07.json)、[两份 DOI 注册记录](tuples_datacite_metadata_batch07.json)。下载后先读外层来源说明，再配合两份原包使用。

## 采集、传输身份与发布

[第 07 批 Release](https://github.com/djxxju/UC_datas_codex/releases/tag/official-data-2026-10-17-batch07) 已公开；[GitHub Actions 运行 39003204769](https://github.com/djxxju/UC_datas_codex/actions/runs/39003204769)成功，采集提交 `33729253739df0a945efcad423d2f33e14470592`。

| 数据附件 | 字节数 | SHA-256 |
|---|---:|---|
| Comillas-openSDUC-951369aa.zip | 439,164 | `5f4cbf4d41d598e907f59b118f470d5e3b49e4566fd3328d7cd15c2b0fb32d8d` |
| OPTIT-CHP-CHCP-UC-2024.zip | 455,222 | `08e4e32499d9d920980a33778c09a37efd571ac7d7dd668be5122617f4285ef1` |

两个发布包合计 894,386 字节。三个上游文件合计 932,201 字节；OPTIT 外层压缩使发布大小略小，不改变内部 ZIP。Release 另附 ATTRIBUTION.md、source_manifest.json、collection_receipt.json，共五个附件。

实际检查限于：云端按清单取得原文件、OPTIT 两个原 ZIP 的大小和 MD5 匹配官方元数据、记录各文件 SHA-256、读取外层 ZIP 中央目录，以及回执与 GitHub 附件的大小/SHA-256 对应。读取到本机的仅有 7,568 字节回执及小型元数据、管理文档，没有下载原始数据包到本机，也没有本地清理。

证据：[发布附件元数据](github_release_batch07.json)、[云端采集回执](cloud_collection_receipt_batch07.json)、[采集清单](../sources/cloud_collection_2026-10-17_batch07.json)。这些是传输与保存记录，不是数据参数、可行性或最优性验证。

## 新增的仅入口候选

### TAMU DemandResponse

[Texas A&M 作者仓库](https://github.com/tamu-engineering-research/DemandResponse/tree/5e305d2462cbb87adb778fdaaf05502766f92c81)，固定提交 `5e305d2462cbb87adb778fdaaf05502766f92c81`。README 介绍合成 ERCOT、2020 年需求/风光水电时序以及 SCUC、SCED、需求响应代码，依赖 MATPOWER/Gurobi。

已读 README 和完整文件目录，GitHub 许可字段为空，目录未见 LICENSE/COPYING/NOTICE，README 没有明确再分发授权。只登记官方入口，不公开镜像原数据，不将其计入已采集来源。README 引用栏还是占位内容，未补造论文 DOI。证据：[Git 树](tamu_candidate_metadata_batch07.json)、[候选审阅记录](candidate_evidence_batch07.json)。

### PyPSA-stochUC

[原作者仓库](https://github.com/PPGS-Tools/PyPSA-stochUC/tree/783a04c10e95ca3ed7bc4c1926f66f3e2b610c2a)，论文 DOI `10.1016/j.ifacol.2024.07.485`。案例主题是垃圾发电厂、热储能与电池的随机 UC。

固定提交 README 明确说明论文所用电厂热负荷是内部资料，不能公开；建议的通用热负荷替代将形成派生案例。因此本轮只登记工具入口及缺失项，不将论文完整数据记为已收集、不生成替代数据。README 同时区分原论文 `v1.0-alpha`、main 的 Pyomo 版本和仍在开发的 Linopy 分支。证据保存在 [候选审阅记录](candidate_evidence_batch07.json)。

原有 CUC-data、REAL Lab、Federalized Power Market 候选状态未变。国内省级完整系统和独立碳总量约束 UC 原包仍未取得；本轮没有联系作者。
