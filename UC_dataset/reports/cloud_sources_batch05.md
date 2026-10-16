# 第 05 批：水电 UC 与作者 SCUC 研究数据

日期：2026-10-16。当前只采集官方现成数据，不解析参数、不转换、不求解。原始 ZIP 由 GitHub 托管运行器获取，本机只保存脚本、索引、管理文档和少量元数据。

## 华中科技大学水电 UC

- 作者：Jinwen Wang、Hao Zheng、Yan Li、Teng Ma；Huazhong University of Science and Technology。
- 正式数据论文：[Dataset for case studies of hydropower unit commitment](https://pmc.ncbi.nlm.nih.gov/articles/PMC5996229/)，Data in Brief 18 (2018), 139–143；DOI [10.1016/j.dib.2018.03.015](https://doi.org/10.1016/j.dib.2018.03.015)。
- 论文介绍九组水电 UC 算例，一天 96 个 15 分钟时段，附水头、流量、机组运行区间及作者结果。模型类别为水电 UC，不能直接混同为火电燃料成本最小化算例。
- Europe PMC [全文 XML 元数据](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5996229/fullTextXML)列明 `mmc2.xlsx`，`permissions` 为 © 2018 The Authors、CC BY 4.0，未列补充材料的例外限制。本轮据此归档随论文发布的附件；证据见 [元数据摘录](hust_hydropower_metadata_batch05.json)。
- 下载使用 Europe PMC 正式 [supplementaryFiles API](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5996229/supplementaryFiles)。PMC 网页本机访问出现浏览器验证；独立的公开 API 正常提供该开放获取文章的附件包，没有操作或绕过验证码。
- 保留服务端返回的 ZIP 原字节。目录清点用于确认 `mmc2.xlsx` 在包中；不读取工作簿单元格，不把作者结果当成本项目复现解。

## 休斯顿大学 RPG Lab SCUC

- 作者：Arun Venkatesh Ramesh、Xingpeng Li，Renewable Power Grid Lab, University of Houston。
- [机构论文页](https://rpglab.github.io/papers/ArunR_ST-C-V_R-SCUC/)与[作者代码仓库](https://github.com/rpglab/GNN-LSTM_C-V-R-SCUC)互相对应；仓库明确链接 Figshare 完整数据。
- 正式数据：[Figshare 第 2 版](https://figshare.com/articles/dataset/Spatio-Temporal_Deep_Learning-Assisted_Reduced_Security-Constrained_Unit_Commitment/24116394/2)，数据 DOI `10.6084/m9.figshare.24116394.v2`，CC BY 4.0。
- 论文 DOI [10.1109/TPWRS.2023.3313430](https://doi.org/10.1109/TPWRS.2023.3313430)，最终期刊引用为 IEEE TPWRS 39(2), 4735–4746 (2024)；作者仓库亦使用 2023 年在线发表信息。
- 论文报告 IEEE 24、73、118 节点和合成 South-Carolina 500 节点系统。数据包用于 SCUC 与机器学习加速研究，包含预制数据、图样本和模型配套文件。图样本不单独计为 UC 系统。
- 原包 `Spatio-TemporalUCAcceleration_GNNLSTM.zip`：1,152,197,046 字节，官方 MD5 `62c1278a8389520fd9004ee3923a6d8a`。固定版本元数据见 [Figshare API 记录](rpglab_figshare_metadata_batch05.json)。
- 观察到作者仓库提交 `d9fb2a1c92c86b9d16c8fa30372b74cd3c86d89e`；它仅有 IEEE24 数据目录及模型示例，因此本批选用 Figshare 完整包。这个提交号是来源关联记录，不冒充 Figshare ZIP 的 Git 版本号。
- 上游说明使用 Python/Pyomo、CPLEX/Gurobi；本项目没有安装、运行或认证该环境。当前本机主求解器仍是 COPT，Gurobi 已登记为未来兼容目标。

## 发布与溯源

[第 05 批 Release](https://github.com/djxxju/UC_datas_codex/releases/tag/official-data-2026-10-16-batch05) 已公开，工作流提交 `dc4f3645cc7ae8190ad7dc4de632c84637045679`，对应 [云端运行](https://github.com/djxxju/UC_datas_codex/actions/runs/38842320204) 成功。两包合计 1,153,213,450 字节，另附三个说明/溯源文件。

| 包 | 已发布字节数 | SHA-256 |
|---|---:|---|
| HUST 水电补充材料 | 1,016,404 | `1690957d09514f55ac2056abd04137a8fd942db3a246a3ecd2bc7cae0bbb0eab` |
| RPG Lab Figshare V2 | 1,152,197,046 | `3fbfa3421e9e330278d954e0fb137b204693b8675230de87e2205e0db1b6d622` |

水电包中央目录含六个文件，确认 `mmc2.xlsx` 为 140,647 字节，另有图像与透明度附件。RPG 包中央目录含 14,087 个文件，确认 `Data/IEEE24Bus`、`IEEE73Bus`、`IEEE118Bus`、`IEEE500Bus` 四个目录；`IEEE500Bus` 是上游文件夹名，论文将系统描述为合成 South-Carolina 500 节点，不能因此称为 IEEE 标准系统。包内大量图样本、已训练模型和参考结果不重复算作独立 UC 实例。

[云端采集回执](cloud_collection_receipt_batch05.json)已读取并与 [GitHub 附件元数据](github_release_batch05.json)核对大小和 SHA-256 一致；RPG 包下载字节的 MD5 与 Figshare 官方元数据一致。没有把两个 ZIP 下载到本机。

[固定采集清单](../sources/cloud_collection_2026-10-16.json)记录 URL、版本、许可和引用。每个 ZIP 原字节保留不变；外置 ATTRIBUTION、manifest、receipt 记录出处和传输身份。只读取 ZIP 中央目录以确认归档成员，不解析 UC 数据或执行上游代码。SHA-256、MD5、文件大小和 MIME 检查服务于传输溯源，不构成模型质量验证。

[尚待镜像的来源](official_candidates_batch05.md)：REAL Lab 的官方工作簿和结果包可访问，但与 CUC-data 一样，明确再分发许可仍待补齐。
