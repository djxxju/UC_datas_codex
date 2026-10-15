# 第 04 批：GitHub 为主要保存位置

日期：2026-10-15。固定发布：[official-data-2026-10-15-batch04](https://github.com/djxxju/UC_datas_codex/releases/tag/official-data-2026-10-15-batch04)。

本批由 GitHub 托管运行器从官方站点获取原件，发布 4 个数据包和 3 个说明/回执附件。本机仅保存脚本、清单和管理文档；两个新增来源的原始数据未下载到本机。

| 数据包 | 新增覆盖或用途 | 原始内容 | 发布包字节数 |
|---|---|---|---:|
| Stochastic-UC-solar-h7cnt32kys-v1.zip | 高比例光伏的随机 UC 研究实例 | 作者发布的 7 个 JSON/HDF5 文件 | 39,444,519 |
| Monash-capacity-expansion-UC-v2.zip | 含 UC 的发电、输电和储能扩展规划 | 6 个原始 XLSX：6bus、6busww、14bus、15bus、21bus、24bus | 1,631,015 |
| RTS-GMLC-v0.2.3.zip | 将此前本地保存的完整官方包归档到 GitHub | 固定提交官方 ZIP，未拆包 | 84,452,206 |
| Tejada-UC-data-1b417ece.zip | 补齐作者完整库在 GitHub 的归档，包括工作簿 | 固定提交官方 ZIP，未拆包 | 4,613,427 |

前两个是新来源；后两个是已有来源的远端归档扩充，不计为新增独立系统。为了便于下载，两个新来源的原文件被装入 ZIP，添加 SOURCE_NOTICE.md 和 SOURCE_METADATA.json；原文件内容未变，未转换格式。

## 新增来源的出处与引用

**Stochastic UC data files**：Kate Doubleday、Bri-Mathias Hodge、Jose Daniel Lara，2022，Mendeley Data V1，DOI [10.17632/h7cnt32kys.1](https://doi.org/10.17632/h7cnt32kys.1)。[作者正式数据记录](https://data.mendeley.com/datasets/h7cnt32kys/1)标注 CC BY 4.0，机构包括 NREL、UC Berkeley 和 University of Colorado Boulder。数据对应高比例太阳能下灵活性措施的随机 UC 研究，供 HodgeLab/Unit_Commitment 与 NREL-SIIP/ExtremeSolarTexas 使用。文件名中出现 validation_descriptors 是上游文件名称，不表示本项目做过验证。

**Monash 数据集**：Semini Wijekoon、Ariel Liebman、Simon Dunstall，2019，*Data Set for Capacity Expansion Planning with Unit Commitment*，版本 2，DOI [10.26180/5cdbde51bbb1b](https://doi.org/10.26180/5cdbde51bbb1b)。[机构数据页](https://bridges.monash.edu/articles/dataset/Data_Set_for_Capacity_Expansion_Planning_with_Unit_Commitment/8131529/2)和[固定版本 API](https://api.figshare.com/v2/articles/8131529/versions/2)标注 CC BY 4.0。官方说明包含 UC 成本/技术参数、DC 网络和全年逐小时负荷/新能源曲线，面向扩展规划；本轮保留六份原始工作簿，不声称已形成统一 JSON 数据集或基础 UC 可直接求解输入。

## 发布与本地空间

- [GitHub Actions 运行](https://github.com/djxxju/UC_datas_codex/actions/runs/38758636950)：成功。
- [发布附件记录](github_release_batch04.json)：官方资产 URL、字节数和 GitHub 返回的 SHA-256。
- [云端采集回执](cloud_collection_receipt_batch04.json)：原文件来源、实际字节数、SHA-256、时间。
- [本地清理记录](local_cleanup_completed_batch04.json)：70 个已经存在可靠 GitHub 副本的本地文件已删除，释放 112,287,926 字节，约 112.3 MB。包括 PGLIB 的 63 个原件、Tejada 的 5 个原件，以及 RTS/Tejada 两个完整原包。每项都有固定恢复地址。
- 没有删除 GitHub 仓库中的 PGLIB/Tejada 原件。许可尚不明确且未镜像的 UC.jl/CommaLAB 旧原件仍保留本地，不新增大规模本地下载。

只核对传输长度、远端保存状态和清理前文件身份，以避免丢失原件；未做 UC 参数检查、格式转换、建模、求解或基准结果复现。采集脚本只做 Python 语法检查，实际下载发布通过云端流程运行完成。

## 继续登记的官方线索

| 来源 | 已确认的现成材料 | 当前状态 |
|---|---|---|
| [datejada/CUC-data](https://github.com/datejada/CUC-data/tree/624abbbdc9f83095c02b34174e52c76f77ddfa36) | 改造 IEEE39/118 的两个聚合 UC 工作簿、GAMS 模型、补充 PDF、README | 固定版本入口已登记；根目录未提供许可证，暂不镜像、不新增本地原件 |
| [华盛顿大学 REAL Lab](https://labs.ece.uw.edu/real/gams_code.html) | 确定性、区间、鲁棒、随机 UC 的 GAMS 模型，输入与上游输出文件；基于 RTS-96 加风电的研究系统 | 官方页和说明已找到；暂只登记，许可及完整下载待后续处理 |
| [华中科技大学水电 UC 数据论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC5996229/) | *Dataset for case studies of hydropower unit commitment*，DOI 10.1016/j.dib.2018.03.015；公开记录列出 mmc2.xlsx 补充数据 | 已找到作者发表记录和附件线索；尚未取得附件，不算已采集。不是已经确认的国内省级综合电网库 |

本次还查看了 CommaLAB 包的文件名及 RCUC/ReadMe.txt 以寻找许可说明，未发现独立再分发声明；没有读取实例参数。该 ReadMe 提及格式文档的勘误，保留为后续适配时需要阅读的上游说明，不在本轮处理。

后续应建立新批次并使用新的 Release 标签，避免覆盖本批固定原件。优先补充国内水电/鲁棒 UC 的正式附件与许可，不重复下载同源日场景凑数。
