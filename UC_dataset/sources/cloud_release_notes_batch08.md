# 官方 UC 相关原始材料：第 08 批

按用户要求继续收集官方已整理资料。本批由 GitHub 托管运行器直接获取原始 ZIP，保留完整源码、数据、文档与许可；不先下载到用户电脑。

- **Comillas IIT openTEPES**：固定提交 `5c0187063874cca4bc7af8ff97b19c6c316dd7a5`，17 个随包示例目录（737 文件）及两类论文配套目录。模型涵盖网络约束 UC、扩展规划、储能、多能耦合及排放约束。目录数不是独立 UC 系统数；RTS 系列与已有来源存在系统重叠。许可 AGPLv3。
- **GenX 官方示例**：固定提交 `3d9596ad9ce69e66ed0404754e58250059bf612b`，11 个示例目录（240 文件），含 UC 相关规划、储能和碳政策资料。存在 UC 线性松弛、政策罚项和 DC OPF 示例，不能将全部目录标为整数 UC 基准。许可 GPLv2。

上述文件数由固定 Git 树统计，归档包范围及下载摘要以附件 collection_receipt.json 为准。仅核对来源、传输、压缩包目录和文件身份，不核验参数、可行性或最优性，不运行 COPT/Gurobi。

下载数据用 `Comillas-openTEPES-5c018706.zip` 或 `GenX-official-examples-3d9596ad.zip`；ATTRIBUTION.md、source_manifest.json、collection_receipt.json 为配套溯源文件。GitHub 自动生成的 Source code ZIP 不含这些独立数据附件。
