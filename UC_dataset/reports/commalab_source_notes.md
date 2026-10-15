# 比萨大学 CommaLAB：现成 UC 算例来源

登记日期：2026-10-15。来源机构：意大利比萨大学计算机科学系 CommaLAB。官方页面标注最后更新为 2022-12-07；页面及压缩包未提供本项目可引用的固定提交号。

## 官方已整理的数据包

以下规模和分类来自[官方 UC 数据页](https://commalab.di.unipi.it/datasets/uc/)，本轮仅确认来源说明与实际页面中的下载地址，未执行数据参数检查、建模或求解。

| 数据包 | 官方描述 | 直接下载 |
|---|---|---|
| RCUC.tgz | 确定性纯火电及水火 UC；最多 300 个机组，其中最多 200 个火电机组；包含爬坡约束 | [RCUC.tgz](https://commalab.di.unipi.it/files/Data/UC/RCUC.tgz) |
| RCUC2.tgz | 纯火电 UC，10–50 个机组 | [RCUC2.tgz](https://commalab.di.unipi.it/files/Data/UC/RCUC2.tgz) |
| 118_UC.tgz | 8 个实例，每例 54 个火电机组；24、36、48、72 时段各 2 例；由两种 IEEE118 基础实例扩展负荷形成 | [118_UC.tgz](https://commalab.di.unipi.it/files/Data/UC/118_UC.tgz) |
| System_46buses.zip | 5 个巴西水火系统背景的随机 UC 实例 | [System_46buses.zip](https://commalab.di.unipi.it/files/Data/UC/System_46buses.zip) |

官方说明确定性实例的格式文档 `Format.pdf` 随实例分发；随机实例另有[输入格式说明](https://commalab.di.unipi.it/files/Data/UC/Structure_input_data.pdf)，采用 `.txt` 文本数据。以上是已生成的数据包，无需自行运行随机生成器。`118` 是来源系统名称，不表示有 118 台机组，也不据此认定已具备某种网络安全约束。

同页另列 [ucig.tgz](https://commalab.di.unipi.it/files/Data/UC/ucig.tgz)，这是支持 XML 输出的 C++ 生成器，单独列作工具，不计入现成实例数据包。

## 引用与使用边界

官方页面把 RCUC 对应至 Frangioni、Gentile 等 2006–2016 年系列研究；RCUC2 对应 Bacci 等 2020、2023 年研究；118_UC 对应 2023 年研究；随机组对应 Scuzziato、Finardi、Frangioni 2018、2021 年研究。论文完整书目信息以[官方页 Bibliography](https://commalab.di.unipi.it/datasets/uc/)为准；本轮不补写未经检索的 DOI。

本轮读取的官方页面未列出明确的数据再分发许可证；公开下载入口本身不等同于再分发授权。当前可公开登记入口和来源说明，原始包是否镜像上传需依据包内许可或其他官方授权，不能自行标为 MIT、BSD 或 CC。下载状态以采集清单为准，本说明不声称包已全部下载或验证。

本来源提供的是上游原生实例格式；本项目尚未实现其 COPT 读取及建模适配，也未确认其可直接输入 Gurobi、CPLEX 或 UnitCommitment.jl。
