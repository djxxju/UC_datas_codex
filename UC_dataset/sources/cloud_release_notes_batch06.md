# 官方 UC 原始资料：2026-10-16，第 06 批

由 GitHub 托管运行器获取三个研究机构/作者来源，保留原格式与版本：

- JRC Dispa-SET EnVarClim 输入数据：原始 ZIP、YAML 配置模板、README 共三个文件；气候年 1990–2015，区域电力系统、水电/水库及燃料/CO2 价格输入。DOI 10.5281/zenodo.3775569，CC BY 4.0。
- Dispa-SET 欧洲部门耦合数据：作者正式 7z，包含配套数据和研究所用模型版本；上游关键词含电动车、热储能和水电。DOI 10.5281/zenodo.3627259，数据 CC BY 4.0，保留包内软件原许可。
- TU Graz LEGO：固定提交 `eb0cb5d478305bfd97c2f2ae952c01fcf87db743` 的官方完整仓库包；含三份预制算例 ZIP、GAMS、手册、原始 MIT 许可及旧版资料。DOI 10.1016/j.softx.2022.101141。

JRC 三个原文件只增加外层 ZIP 与来源说明；其内部 ZIP 不展开。其他两个压缩包保持下载字节不变，仅使用易识别的 Release 附件名称。

当前完成的是采集与归档：未转换参数、未运行宏或上游程序、未调用 COPT/Gurobi/CPLEX。保留原始模型用途；部门耦合和扩展规划数据不混称为普通日前火电 UC；排放价格不等于已实现排放总量约束。

原件来源、许可、下载日期和哈希见 ATTRIBUTION.md、source_manifest.json、collection_receipt.json。本机不先下载原始大包。旧 Release 和旧原件保留。
