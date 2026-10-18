# 第 10 批：UC.jl 已确认许可子集归档

日期：2026-10-18。按计划继续官方原件收集。本批将既有 UnitCommitment.jl 来源组从仅本地保存推进到部分 GitHub 镜像，没有增加独立来源组、生成算例或转换数据。

## 许可核查与范围

读取旧本地 117 个 .json.gz，仅提取顶层 LICENSE 和 SOURCE 元字段；全部原始字节的大小与 SHA-256 均匹配 2026-10-15 采集回执。没有校验 UC 数值参数。

| 已有系列 | 文件数 | 本次证据 | 归档结论 |
|---|---:|---|---|
| OR-LIB | 42 | 每个 JSON 内含同一完整 MIT 许可；[OR-Library 官方许可页](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/legal.html)明确适用于该库资料 | 全部进入第 10 批 |
| Tejada19 | 49 | 每个 JSON 内含完整 MIT，Copyright (c) 2018 Diego Alejandro Tejada Arango | 全部进入第 10 批 |
| MATPOWER 代表日 | 26 | 所选原件未带顶层 LICENSE；本轮未找到足以确认其独立再分发条款的证据 | 旧本地原件与官方地址保留，未公开镜像 |

本次依据是各数据文件自带的许可证，未从 UC.jl 软件许可证推断全部外部数据许可。未内嵌 LICENSE 不表示永远不能再分发，仅表示本轮尚未确认。

完整通知按原文保留于 [OR-LIB 许可](../sources/licenses/ucjl_0.4/ORLIB_LICENSE.txt)、[Tejada19 许可](../sources/licenses/ucjl_0.4/Tejada19_LICENSE.txt)和每个原件中。外层 SOURCE_METADATA.json 也附完整许可。OR-Library 原文的标点与拼写未修改。

逐文件证据：[许可核查记录](ucjl_license_audit_batch10.json)。OR-LIB 许可文本 SHA-256：9281d1929b8b3ae9545151b505db99128a2d633eab18744911eccc24bec2616d；Tejada19：4c64953e7738fc4f1f439069238cbf30b47d8aa0ec2a5dc9386673e53eab7161。

## 下载与原件位置

[第 10 批 Release](https://github.com/djxxju/UC_datas_codex/releases/tag/official-data-2026-10-18-batch10)已公开，包含两个数据 ZIP 和三份溯源附件：

| 数据包 | 原始 .json.gz 数 | 发布大小（字节） | 下载 |
|---|---:|---:|---|
| UCjl-v0.4-ORLIB-42-instances.zip | 42 | 450953 | [下载 OR-LIB](https://github.com/djxxju/UC_datas_codex/releases/download/official-data-2026-10-18-batch10/UCjl-v0.4-ORLIB-42-instances.zip) |
| UCjl-v0.4-Tejada19-49-instances.zip | 49 | 2804575 | [下载 Tejada19](https://github.com/djxxju/UC_datas_codex/releases/download/official-data-2026-10-18-batch10/UCjl-v0.4-Tejada19-49-instances.zip) |

原始文件共 3,232,913 字节；外层包合计 3,255,528 字节。每包根目录为原 .json.gz 文件、SOURCE_NOTICE.md 和 SOURCE_METADATA.json。解压外层后仍保留 gzip 压缩；可用支持 gzip 的读取器查看 JSON。此操作只读取文件，不构成模型导入验证。

例如 OR-LIB 包中的 10_0_1_w.json.gz，可在 Python 中用 gzip.open(path, 'rt', encoding='utf-8') 配合 json.load 读取。原件索引逐条记录包下载地址、包内文件名及原件 SHA-256：[实例索引](../sources/ucjl_available_instances.json)。

## 版本与引用

- 官方代码文档版本 v0.4.2，提交 e4cc95dae16d9b8bccbfcd95ccf754b307d66c4a；[固定版本实例说明](https://github.com/ANL-CEEESA/UnitCommitment.jl/blob/e4cc95dae16d9b8bccbfcd95ccf754b307d66c4a/docs/src/guides/instances.md)。
- 实例服务器版本 0.4。版本目录不是不可变 Git 提交，实际归档身份以本项目逐文件 SHA-256 为准。云端必须与已核查许可的旧原件完全一致才发布。
- OR-LIB 原件 SOURCE 引用 Beasley (1990), DOI 10.2307/2582903，以及 Frangioni & Gentile (2006), DOI 10.1287/opre.1060.0309。
- Tejada19 原件 SOURCE 引用 Tejada-Arango et al., Which Unit-Commitment Formulation is Best? A Systematic Comparison, DOI 10.1109/TPWRS.2019.2962024。
- 使用时同时按官方实例说明引用 UnitCommitment.jl 和原始算例来源。保留内嵌许可与引用。

Tejada19 是 UC.jl 提供的转换表示，与第 04 批作者 UC-data 同源。OR-LIB/Tejada19 两包属于已有 UC.jl 来源组，不额外计算两个新来源组。PGLIB 转换条目未重复采集；MATPOWER 全年场景也未采集。

## 实际执行与核对

[云端运行 39115108285](https://github.com/djxxju/UC_datas_codex/actions/runs/39115108285)成功，采集提交 0363a43af2107606a2658373f16a2469fe61d96b。发布前逐个读取 ZIP 成员的压缩原件字节并比较已核查 SHA-256，91/91 通过；不解压 gzip 或解释数值参数。外层分别有 44/51 个文件，含各两份本项目包装说明，不是算例数。

本机只新增回执及文档等小型元数据，没有新增原始数据副本，也没有删除旧原件。下载的回执 94,578 字节，SHA-256 267c5da6eb48b72fa97034e64530fa47b685f7dbbb83538e8c6841aecfba4036，与 GitHub 附件摘要一致。两个数据包大小与 GitHub SHA-256 均匹配回执，91 个原件的回执大小/SHA-256 均匹配本地许可核查记录。

新增文件身份检查脚本使用临时合成字节测试：匹配样本通过，错误哈希、缺少/多余预期文件均被拒绝；这些测试不使用 UC 参数，也不是求解测试。

证据：[云端回执](cloud_collection_receipt_batch10.json)、[GitHub 发布记录](github_release_batch10.json)、[发布核对](publication_audit_batch10.json)、[采集清单](../sources/cloud_collection_2026-10-18_batch10.json)、[工作流](../../.github/workflows/collect-official-data-batch10.yml)。

## 当前完成程度与下一入口

累计 17 个来源组取得原件：15 个所选范围已在 GitHub 保存，UC.jl 一个来源组部分镜像，CommaLAB 一个来源组仍仅有旧本地原件；即 16 个来源组已有至少部分 GitHub 原件。Release 数据附件从 14 个增至 16 个，另有 PGLIB 原件目录。七个仅入口候选未改变。

原件线仍处阶段二收集。没有 UC 参数校验、统一格式转换、COPT/Gurobi 模型运行或基准解复现；独立标准化库的派生试点继续按其自身计划推进，本轮未改动。

下一步优先补查 FERC 公开冬夏资料附件和明确许可的需求响应/国内完整 UC 研究包。MATPOWER 衍生文件与 CommaLAB 的再分发证据继续保留为未完成事项，未获新证据前不批量镜像全年文件。
