> 第 04 次工作更新：完整官方归档已发布到 [GitHub Releases](https://github.com/djxxju/UC_datas_codex/releases/tag/official-data-2026-10-15-batch04)；确认远端副本后已清理本地重复原件。下文原采集过程保留为历史记录，当前存储状态以 [来源登记](../sources/source_registry.json)为准。

# Tejada 作者发布的现成 UC 数据包

登记日期：2026-10-15。本轮收集官方来源与原件；未检查参数、转换模型或求解。

## 首选原始包

作者仓库：[datejada/UC-data](https://github.com/datejada/UC-data)。README 明确关联论文 DOI [10.1109/TPWRS.2019.2962024](https://doi.org/10.1109/TPWRS.2019.2962024)，并说明 `UC-Instances.zip` 是使用比萨大学 UC 生成工具预先生成的数据。用户可直接获取作者生成好的包，无须自己运行生成器。

本次登记固定提交：`1b417ece7ca61d41fca7302df6a0313f8236d611`（上游提交日期 2020-02-13）。下表大小及 Git blob SHA 来自 GitHub 官方文件元信息，并非本项目下载后计算的哈希。

| 文件 | 官方大小（字节） | 用途 | 固定版本下载入口 |
|---|---:|---|---|
| UC-Instances.zip | 1,069,070 | 作者已生成的 UC 实例包，ZIP 内部格式本轮未检查 | [下载](https://raw.githubusercontent.com/datejada/UC-data/1b417ece7ca61d41fca7302df6a0313f8236d611/UC-Instances.zip) |
| UC-Instances-ResultsSummary.zip | 1,899,047 | 作者发布的结果汇总包；仅登记为上游结果，不作为本项目复现结果 | [下载](https://raw.githubusercontent.com/datejada/UC-data/1b417ece7ca61d41fca7302df6a0313f8236d611/UC-Instances-ResultsSummary.zip) |
| StarGenLite_SCUC.gms | 44,815 | 配套 GAMS 模型 | [下载](https://raw.githubusercontent.com/datejada/UC-data/1b417ece7ca61d41fca7302df6a0313f8236d611/StarGenLite_SCUC.gms) |
| StarGenLite_SCUC_10gen.xlsm | 2,339,962 | 作者命名的 10gen 工作簿 | [下载](https://raw.githubusercontent.com/datejada/UC-data/1b417ece7ca61d41fca7302df6a0313f8236d611/StarGenLite_SCUC_10gen.xlsm) |
| StarGenLite_SCUC_54gen.xlsm | 2,478,768 | 作者命名的 54gen 工作簿 | [下载](https://raw.githubusercontent.com/datejada/UC-data/1b417ece7ca61d41fca7302df6a0313f8236d611/StarGenLite_SCUC_54gen.xlsm) |
| StarGenLite_SCUC_200gen.xlsm | 2,476,926 | 作者命名的 200gen 工作簿 | [下载](https://raw.githubusercontent.com/datejada/UC-data/1b417ece7ca61d41fca7302df6a0313f8236d611/StarGenLite_SCUC_200gen.xlsm) |
| StarGenLite_SCUC_800gen.xlsm | 2,659,882 | 作者命名的 800gen 工作簿 | [下载](https://raw.githubusercontent.com/datejada/UC-data/1b417ece7ca61d41fca7302df6a0313f8236d611/StarGenLite_SCUC_800gen.xlsm) |

前两个 ZIP 的上游 Git blob SHA 分别是 `7a2f0916d0628e66eb7cea5799ff0373f464a1a3`、`3ce815e2ba77e5b9c313509b066014997ff59731`。采集时应一并保存 [README](https://raw.githubusercontent.com/datejada/UC-data/1b417ece7ca61d41fca7302df6a0313f8236d611/README.md) 和 [MIT LICENSE](https://raw.githubusercontent.com/datejada/UC-data/1b417ece7ca61d41fca7302df6a0313f8236d611/LICENSE)，保留作者版权声明。

## 与已登记库的关系

[UnitCommitment.jl 官方 Tejada19 说明](https://anl-ceeesa.github.io/UnitCommitment.jl/0.2/instances/#Tejada19) 将该系列指向同一论文，并解释其使用与 OR-LIB/UC 相同的随机生成器，规模更大。本项目已经登记的 49 个 UC.jl Tejada 条目是转换版本，不能与作者原包重复计为 49 个新增独立系统。原包与转换版本的逐文件映射留待以后处理。

作者机构的[论文摘要](https://www.iit.comillas.edu/documentacion/revista/IIT-18-110A_preview/Which_unit-commitment_formulation_is_best?+A+comparison+framework.pdf=) 描述研究实验共 54 个实例、10—1888 台机组、24/168 小时。这个数字是论文实验范围，不作为本轮对 ZIP 内容的实测计数，也不能直接解释为 UC.jl 的 49 个转换条目。

## 可选扩展来源

同一作者另有 [datejada/CUC-data](https://github.com/datejada/CUC-data)：README 发布两个聚合机组组合算例（改造 IEEE39、IEEE118），原格式为 XLSX，附 GAMS 代码和补充说明。论文 DOI [10.1109/TPWRS.2019.2908051](https://doi.org/10.1109/TPWRS.2019.2908051)。本轮只登记入口；页面未显示独立许可证，不将其默认为 UC-data 的 MIT 授权范围。

## FERC 原始入口的边界

[FERC RTO Unit Commitment Test System 官方页](https://www.ferc.gov/power-sales-and-markets/increasing-efficiency-through-improved-software/rto-unit-commitment-test) 提供冬、夏公开场景的 eLibrary 入口（docket AD10-12-002）。该页面明确网络文件与 GAMS 模型受到 CEII 获取限制，所以不把完整 FERC 网络 UC 系统列为无需手续即可下载的公开现成包。当前优先使用已经收齐的 PGLIB-UC FERC 系列；FERC 原始入口作为溯源资料登记，不绕过获取限制。

## 本项完成状态

已下载固定提交的官方仓库整包（4,613,427 字节），并从外层仓库 ZIP 原样取出两个数据/结果 ZIP、GAMS 模型、README、LICENSE，保存至 `raw/tejada_author/1b417ece7ca61d41fca7302df6a0313f8236d611/`。两个内部 ZIP 没有打开，模型没有运行。采集记录见 [回执](tejada_collection_20261015T144032865220Z.json)；本批已将五个原件连同许可一起公开。
