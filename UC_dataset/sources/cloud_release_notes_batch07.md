# 官方 UC 原始材料：第 07 批

本批通过 GitHub 云端采集，包含两组来源、三个上游原始文件：

- **Comillas IIT openSDUC**：固定提交 `951369aad1615fc6c2281d7bd350ded393096f3a` 的官方仓库整包，含文档所称 16 机组示例、17 个 CSV 输入/字典文件、Python/Pyomo 源码与完整 AGPLv3 许可。
- **OPTIT / 博洛尼亚大学 CHP–CHCP 测试材料**：2024-03-26 两份 Zenodo 正式记录配套归档，含 `data.zip` 与 `base_instance.zip`。作者说明前者有 2022 年的 365 个逐日 JSON；两份互补资料合并统计为一个来源组，不计作两个独立系统。两者均为 CC BY 4.0。

## 下载与使用入口

展开 Assets 下载 `Comillas-openSDUC-951369aa.zip` 或 `OPTIT-CHP-CHCP-UC-2024.zip`。同时保存 ATTRIBUTION.md、source_manifest.json 和 collection_receipt.json。

openSDUC 解压后先读 README.md、LICENSE、doc/md/InputData.md；数据在 openSDUC/16g。OPTIT 外层解压后保留两个原 ZIP 及 SOURCE_NOTICE.md、SOURCE_METADATA.json，设备描述与逐日输入应一起使用。

仅进行原件传输、文件身份记录和 ZIP 外层目录清点。未转换格式、校验 UC 参数、安装依赖或运行 COPT/Gurobi。上游求解器支持不等于本项目适配已完成。365 日输入不代表 365 个独立电网。

openSDUC 的根 LICENSE/README/说明是 AGPLv3，pyproject.toml classifier 写为 GPLv3+；原样保留并披露该上游元数据差异，不重新授权。完整源码和许可随包保留。

出处、许可、引用、原文件大小/MD5 及逐文件 SHA-256 见随包溯源文件。原文件字节不变；OPTIT 仅增加外层封装及来源说明。
