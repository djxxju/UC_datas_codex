# 尚未建立原件镜像的官方来源：第 05 批核对

核对日期：2026-10-16。此表为事实性索引，不计入“已有原件”的来源数量。

## 华盛顿大学 REAL Lab

[实验室正式入口](https://labs.ece.uw.edu/real/gams_code.html)提供确定性、改进区间、区间、鲁棒和随机 UC 的 GAMS 模型，以及共用输入、鲁棒输入、输入工作簿、作者结果包。上游要求引用：H. Pandzic, Y. Dvorkin, T. Qiu, Y. Wang, D. Kirschen, *Unit Commitment under Uncertainty – GAMS Models*, REAL, University of Washington, Seattle, USA。

页面原链接使用 `www.ee.washington.edu/research/real/Library/Code/`；现行机构地址位于 `labs.ece.uw.edu/real/Library/Code/`。

| 材料 | 现行机构链接 | 本轮记录 |
|---|---|---|
| 说明 | [UnitCommitmentunderUncertainty-GAMSModels.pdf](https://labs.ece.uw.edu/real/Library/Code/UnitCommitmentunderUncertainty-GAMSModels.pdf) | 上游模型说明入口 |
| 确定性模型 | [Deterministic_UC.gms](https://labs.ece.uw.edu/real/Library/Code/Deterministic_UC.gms) | 临时读取代码文本查许可，没有执行或持久保存 |
| 改进区间模型 | [Improved_Interval_UC.gms](https://labs.ece.uw.edu/real/Library/Code/Improved_Interval_UC.gms) | 来源页链接 |
| 区间模型 | [Interval_UC.gms](https://labs.ece.uw.edu/real/Library/Code/Interval_UC.gms) | 来源页链接 |
| 鲁棒模型 | [Robust_UC.gms](https://labs.ece.uw.edu/real/Library/Code/Robust_UC.gms) | 来源页链接 |
| 随机模型 | [Stochastic_UC.gms](https://labs.ece.uw.edu/real/Library/Code/Stochastic_UC.gms) | 来源页链接 |
| 共用输入 | [Input_Data.gms](https://labs.ece.uw.edu/real/Library/Code/Input_Data.gms) | 来源页链接 |
| 鲁棒输入 | [Input_Data_for_Robust_UC.gms](https://labs.ece.uw.edu/real/Library/Code/Input_Data_for_Robust_UC.gms) | 来源页链接 |
| 全部输入工作簿 | [input_UC_ii.xlsx](https://labs.ece.uw.edu/real/Library/Code/input_UC_ii.xlsx) | HEAD 200；10,249,059 字节；未下载正文 |
| 作者结果包 | [UC_schedule.zip](https://labs.ece.uw.edu/real/Library/Code/UC_schedule.zip) | HEAD 200；4,861,337 字节；未下载正文 |

所读页面及确定性代码文本未发现明确再分发许可。“使用时请引用”没有被当成通用再分发许可证。当前仅整理链接，未把输入工作簿和结果包上传本仓库；HEAD 信息不是原件采集成功或参数验证。

本机 Python 默认 TLS 证书链无法验证该站；PowerShell 系统证书验证可正常读取。未关闭 TLS 验证、未改变系统代理。

## 作者 CUC-data

[固定版本入口](https://github.com/datejada/CUC-data/tree/624abbbdc9f83095c02b34174e52c76f77ddfa36)。作者提供改造 IEEE39 和 IEEE118 的两个聚合 UC 工作簿、GAMS 模型和 Addendum。

- [CUC_IEEE39-busSystem.xlsx](https://github.com/datejada/CUC-data/blob/624abbbdc9f83095c02b34174e52c76f77ddfa36/CUC_IEEE39-busSystem.xlsx)：76,923 字节，上游文件元数据。
- [CUC_IEEE118-busSystem.xlsx](https://github.com/datejada/CUC-data/blob/624abbbdc9f83095c02b34174e52c76f77ddfa36/CUC_IEEE118-busSystem.xlsx)：145,652 字节，上游文件元数据。
- 论文 DOI：[10.1109/TPWRS.2019.2908051](https://doi.org/10.1109/TPWRS.2019.2908051)。

根目录未列 LICENSE，README 未载许可；本轮查看 `StarGenLite_Clustered-UC.gms` 的作者头部并搜索许可关键词，也没有找到授权条款。没有把同一作者另一仓库 UC-data 的 MIT 许可套用到此仓库。仍未采集或镜像这两个工作簿，未运行 GAMS。

## 待续

继续查找上游公开的独立数据授权说明；当前可保留正式下载入口，后续有明确证据再建立镜像。UC.jl 外部实例和 CommaLAB 的再分发状态仍沿用上一批，未声称本轮已解决。
