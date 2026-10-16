# 官方 UC 原始数据包：2026-10-16，第 05 批

新增两个原作者/研究机构来源，均保留原始 ZIP 字节，由 GitHub 云端下载并归档：

- 华中科技大学水电 UC：Europe PMC 正式补充材料包，含 `mmc2.xlsx`；论文介绍九组 15 分钟水电 UC 算例与作者参考结果。DOI 10.1016/j.dib.2018.03.015，CC BY 4.0。
- 休斯顿大学 RPG Lab：Figshare V2 完整 SCUC 研究包，1,152,197,046 字节；论文覆盖 IEEE 24/73/118 与合成 South-Carolina 500 节点。数据 DOI 10.6084/m9.figshare.24116394.v2，CC BY 4.0。

来源、引用、下载日期、大小和 SHA-256 见 `source_manifest.json`、`ATTRIBUTION.md`、`collection_receipt.json`。ZIP 目录清单仅用来确认附件和归档范围，不解析算例参数。作者结果与机器学习样本保留上游身份，不视为本项目复现解或独立系统。

本批没有修改算例、转换 schema、运行 COPT/Gurobi/CPLEX 或验证可行性与最优性。COPT 是当前本机主求解器；Gurobi 是用户新增明确的后续兼容目标，适配工作暂缓。原始大包未下载到用户本机。
