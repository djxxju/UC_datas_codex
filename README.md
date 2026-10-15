# UC 公开算例库收集与复现

本仓库优先收集可以直接读取和建模的现成 UC 基准，再逐步统一字段、实现 COPT 适配和独立验解。

## 已收集的数据

**PGLIB-UC 全部 56 个算例已归档，63 个上游原始文件逐一通过 Git blob 哈希核对。** 固定提交为 `39a7f38cf4703de92f0291f0c873c2e98c789301`，原始数据未修改，全部为 48 小时、1 小时时间步长。

| 来源系列 | 算例数 | 火电机组数 | 可再生机组数 | 网络 |
|---|---:|---:|---:|---|
| CA | 20 | 610 | 0 或 1 | 无网络 |
| FERC | 24 | 934 或 978 | 1 | 无网络 |
| RTS-GMLC 派生 | 12 | 73 | 81 | 无网络 |

数据目录：[PGLIB-UC 原始库](UC_dataset/raw/pglib_uc/39a7f38cf4703de92f0291f0c873c2e98c789301/)。逐例信息见 [catalog.json](UC_dataset/catalog.json)，校验记录见 [pglib_integrity.json](UC_dataset/reports/pglib_integrity.json)。

数据采用 CC BY 4.0，参考程序采用 MIT；原始许可、文档、数学模型和 Python/Julia 参考实现均保留。引用与使用要求见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## 直接使用

从仓库根目录运行以下命令，只需 Python 标准库：

```powershell
python UC_dataset/validation/inspect_pglib.py
python UC_dataset/examples/read_case.py
```

第一条重新核对全部上游文件哈希并做基础字段检查，第二条读取一个原始 RTS-GMLC 派生算例并输出规模和负荷范围。重新获取 PGLIB-UC 可以运行 `python UC_dataset/sources/collect_pglib.py`，它会从固定提交的官方压缩包获取并核对字节。

上游 `uc_model.py` / `uc_model.jl` 是参考建模程序，依赖相应建模环境；其默认求解器设置需要按实际环境配置。**本机主求解器为 COPT；当前尚未实现并验证 COPT 的 UC 适配器，也未生成本项目基准解。** 本次的“可直接用”指上游已定义好参数和模型的基准数据，无需重新从文献录入参数；并不表示已经通过本机求解验证。

## 更多现成 UC 数据

[UnitCommitment.jl 官方 v0.4.2 实例说明](https://github.com/ANL-CEEESA/UnitCommitment.jl/blob/e4cc95dae16d9b8bccbfcd95ccf754b307d66c4a/docs/src/guides/instances.md)列出 173 个实例入口：26 个 MATPOWER 日样本、56 个 PGLIB-UC 转换实例、42 个 OR-LIB 实例和 49 个 Tejada19 实例。MATPOWER 系列还提供 2017 全年每日变体。这里的 56 个 PGLIB 转换条目与本仓库原始 PGLIB 库有来源重叠，不能算作独立新增系统。

已整理[官方条目索引](UC_dataset/sources/ucjl_available_instances.json)与下载脚本：

```powershell
python UC_dataset/sources/download_ucjl.py or-lib/10_0_1_w
python UC_dataset/sources/download_ucjl.py matpower/case118/2017-01-01
```

下载后保留原始 `.json.gz`，并生成哈希与参数摘要。若本机代理导致连接失败，可为当前下载添加 `--no-proxy`，该选项不修改系统设置。Julia 环境中可按对应版本的官方方法调用 `UnitCommitment.read_benchmark("or-lib/10_0_1_w")`。

本次抽样成功下载并解析了 10 机、20 机、214 机及 IEEE118 实例，原件留在本地。服务器数据的独立再分发许可尚未明确，因此仓库提供获取脚本和事实性索引，不公开镜像这些原件。软件许可不能自动视为外部实例数据许可。旧格式样本可能包含 36 小时以及未显式指定的线路限额，使用时须按版本核对默认规则。

RTS-GMLC 原始系统另列为后续网络和新能源场景来源；原始系统还需明确初始化和时序处理后才能形成目标 UC 实例。当前不计入本仓库可直接读取的 56 个正式归档算例。

## 项目管理

每次开始前阅读[计划书](项目计划书.md)、[项目进度](项目进度.md)和最新[工作日志](工作日志/)；结束时追加总结并更新进度。固定约定见 [AGENTS.md](AGENTS.md)。
