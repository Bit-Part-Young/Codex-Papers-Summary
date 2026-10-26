# 文献总结 - 借助量子加速器推动人工智能时代原子模拟工作流的普及 - 2026

---

## 文献基本信息

- **英文标题**：Democratizing Atomistic Simulation Workflows for the AI Era with the Quantum Accelerator
- **DOI**：原文未提供（文末的 https://doi.org/10.5281/zenodo.7720998 是 QuAcc 软件版本存档的 DOI，并非本文 DOI）。
- **作者**：Andrew S. Rosen、Naisargi Goyal、Brad Ayers、Vineet Bansal、Julia H. Baratta、Samuel M. Blau、Yuan Chiang、Sihoon Choi、Orion Archer Cohen、Blake Dallmann、Tom Demeyere、Will Engler、Yue-Wen Fang、Isabella Furrick、Eliu Huerta、Honghui Kim、Hironori Kondo、Anup Kumar、Jaehong Kwon、Osman Mamun、Charles B. Musgrave III、Hananeh Oliaei、Aryan Saha、Davide Sarpa、Benjamin X. Shi、Yuliang Shi、Xing Wang、Robert B. Wexler。
- **作者单位**：
    - 1 Department of Chemical and Biological Engineering, Princeton University, Princeton, New Jersey 08544, United States
    - 2 School of Chemistry and Chemical Engineering, University of Southampton, Southampton, United Kingdom
    - 3 Research Computing, Princeton University, Princeton, New Jersey 08544, United States
    - 4 Energy Technologies Area, Lawrence Berkeley National Laboratory, Berkeley, California 94720, United States
    - 5 Department of Materials Science and Engineering, University of California, Berkeley, California 94720, United States
    - 6 Materials Sciences Division, Lawrence Berkeley National Laboratory, Berkeley, California 94720, United States
    - 7 Riven Systems, New York, New York 10027, United States
    - 8 Department of Materials Chemistry, Federal Institute of Materials Research and Testing, 12205 Berlin, Germany
    - 9 Globus, University of Chicago, Chicago, Illinois 60637, United States
    - 10 Instituto de Nanociencia y Materiales de Aragón, CSIC-Universidad de Zaragoza, Zaragoza 50009, Spain
    - 11 Data Science and Learning Division, Argonne National Laboratory, Lemont, Illinois 60439, USA
    - 12 Department of Computer Science, The University of Chicago, Chicago, Illinois 60637, USA
    - 13 Graduate School of AI, Korea Advanced Institute of Science and Technology, Seoul, Republic of Korea
    - 14 Harvard John A. Paulson School of Engineering and Applied Sciences, Harvard University, Cambridge, Massachusetts 02138, United States
    - 15 Department of Chemistry and Chemical Biology, Harvard University, Cambridge, Massachusetts 02138, United States
    - 16 Quantum Software Engineering Team, D-Wave Quantum Inc., New Haven, Connecticut 06511, United States
    - 17 R. F. Smith School of Chemical and Biomolecular Engineering, Cornell University, Ithaca, New York 14853, United States
    - 18 Department of Materials Science and Engineering, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, United States
    - 19 Department of Electrical and Computer Engineering, Princeton University, Princeton, New Jersey 08544, United States
    - 20 Initiative for Computational Catalysis, Flatiron Institute, New York, New York 10010, United States
    - 21 Elemynt Pte. Ltd., 3 Fusionopolis Way, Singapore 138633, Singapore
    - 22 Department of Chemistry and Institute of Materials Science and Engineering, Washington University in St. Louis, St. Louis, Missouri 63130, United States
    - 现址（Hironori Kondo）：Department of Materials Science and Engineering and Center for Computational Science and Engineering, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, United States
- **期刊**：原文未提供；所给 PDF 未标注期刊名称。
- **日期**：投稿、返修、接收及在线发表日期均为原文未提供。
- **数据与代码链接**：QuAcc 代码 https://github.com/Quantum-Accelerators/quacc；软件版本 Zenodo 存档 https://doi.org/10.5281/zenodo.7720998。本文基准测试数据的独立下载链接原文未提供。

---

## 论文内容详细总结

### 研究背景与目的

- 人工智能和材料设计推动了高通量原子模拟需求。密度泛函理论（DFT）等量子力学计算既可为性质预测模型提供输入，也可产生机器学习原子间势（MLIPs）的训练与评估数据；基础 MLIPs 则使更大时间、空间尺度的势能曲面探索成为可能。
- 作者将计算基础设施区分为工作流引擎、原子模拟驱动程序和工作流库三层。现有工作流库通常紧密绑定单个引擎，用户的计算需求与该引擎不符时会妨碍采用。研究目标是提供可重现、易扩展、对不同计算环境适用的 QuAcc 工作流库，并使专家和非专家都能使用现成计算配方。
- 论文属于软件架构、功能介绍与实例基准测试相结合的研究论文。PDF 未标注期刊和正式发表信息，也没有独立的 Methods 章节。

---

### 研究方法与软件架构

#### 预定义模拟配方与输出

- QuAcc 以 Atomic Simulation Environment（ASE）为主要原子模拟驱动程序，提供静态计算、结构弛豫以及视软件而定的分子动力学、表面、振动与声子、过渡态搜索和能带计算配方。支持 FHI-aims、Gaussian、MRCC、ONETEP、ORCA、Psi4、Q-Chem、Quantum ESPRESSO、VASP、DFTB+、TBLite 和 GULP 等；通过 Rootstock、matcalc、FAIR-Chem 接入预训练 MLIPs，另有 TorchSim 配方用于 GPU 批量计算。
- 各配方返回包含任务元数据和关键结果的字典，即 schema。ASE 负责输入文件写入及结构、能量、力、应力等读取；需要更丰富数据时复用成熟解析器。Q-Chem 和 VASP 的部分配方默认经 Custodian 处理常见运行错误。

#### 工作流引擎解耦

- 计算任务、工作流及动态子工作流分别用 `@job`、`@flow`、`@subflow` 修饰普通 Python 函数。导入函数时，QuAcc 按用户设置将通用修饰器映射为所选引擎的抽象；不选择引擎时按普通同步函数执行。任务依赖、提交、监控和资源分配由引擎负责。
- 写作时支持 Dask、Jobflow、Parsl、Prefect、Ray、Redun，也可直接执行 Python 函数；适用环境包括本地工作站、高性能计算集群及分布式云资源。为互操作性，作者还处理了任务返回字典的延迟键访问和 ASE Atoms 等对象在不同引擎间序列化的问题。
- 默认 Python 包保持少量依赖，其他依赖按配方分组可选安装。单元与功能测试在写作时接近 100% 行覆盖率；部分易安装量子化学程序进行真实的小规模计算测试，专有程序默认模拟执行，维护者还可在本地计算集群运行未模拟的端到端测试。

---

### 主要结果

#### 工作流实例

- 图 3a 将体相铜的 $2\times2\times2$ 超胞弛豫与静态计算串联，使用 DFTB+ 中带周期边界条件的 GFN2-xTB；无需改写科学代码即可通过设置选择远程引擎。图 3b 串联 TensorNet-MatPES-PBE 势的弛豫与 MatPES 兼容设置下的 VASP 静态计算。图 3c 展示生成高对称表面片、分别弛豫并静态计算的动态工作流；独立的表面片任务可并发运行。

#### MLIP 基准测试设计

- 作者用 QuAcc 对 WBM 高能态数据集中的 100 个结构做单点 DFT 计算。这些结构来自对 WBM 结构在 1000 K 下的分子动力学模拟，覆盖 82 种元素。比较对象是原数据集提供的 WBM DFT 标签和与各 MLIP 训练数据一致的 DFT 设置。
- 五个模型为 TensorNet-MatPES-PBE (2025.2)、MACE-MatPES-PBE-0、MACE-OMat-0 (medium)、PET-OMat-XL (v1.0.0) 和 UMA-OMat-s1p2p1。前两个对应 MatPES-PBE，后三个对应 OMat24。比较指标为能量、力、应力的平均绝对误差（MAE）。

#### 关键定量结果

- 能量 MAE（WBM → 匹配的 DFT，单位 meV/atom）：TensorNet-MatPES-PBE 为 260.8 → 50.4；MACE-MatPES-PBE-0 为 261.7 → 49.7；MACE-OMat-0 为 70.1 → 31.2；UMA-OMat-s1p2p1 为 69.2 → 22.2；PET-OMat-XL 为 69.4 → 19.8。MatPES 模型表观能量 MAE 约降至五分之一，OMat24 模型均降至不足原来的一半。
- 力 MAE（同序，单位 meV/Å）：191.5 → 146.0、168.1 → 117.8、105.2 → 90.1、63.9 → 47.2、55.3 → 38.0。原文概括为约 15–30% 的下降。应力 MAE（同序，单位 GPa）：0.984 → 0.783、1.134 → 0.879、0.756 → 0.739、0.489 → 0.497、0.405 → 0.432，变化较小且方向不一致。
- 作者指出 MatPES 与 WBM 的 Hubbard U 修正设置差异是 MatPES 模型能量差异大的部分原因；不同赝势、交换关联泛函、色散修正等设置也可能造成方法不一致。WBM 的 MPRelaxSet 标签与 OMat24 都采用 $5.0\times10^{-5}$ eV/atom 的自洽场能量收敛准则，这可能影响较大结构的数值收敛，尤其是晶胞应力。

---

### 讨论与结论

- 对预训练 MLIPs 评价时，应使单点 DFT 参考计算尽量与模型训练或微调数据在电子结构程序、泛函、修正方法及赝势或基组上保持一致；否则方法差异会被误判成模型误差。QuAcc 提供对应多个常用数据集的预定义 DFT 配方，以支持内部一致的基准数据及新增训练数据生成。
- 作者认为，随着大语言模型与代理式 AI 参与计算流程构建，配方库可为科学软件调用提供已有的合理默认值与防护。QuAcc 的核心贡献是通过可组合配方及工作流引擎互操作性，降低复杂原子模拟工作流的使用和开发门槛。文中展示了功能与一项基准测试；未提供跨引擎运行性能的系统量化比较。

---

## 章节翻译

### 摘要

我们介绍 Quantum Accelerator（QuAcc），一个面向原子模拟、以量子力学计算为重点的开源工作流库。QuAcc 提供预定义工作流配方，涵盖第一性原理电子结构方法、半经验与紧束缚方法、经典势以及基础机器学习原子间势（MLIPs）。QuAcc 的一个核心设计特征，是将领域特定的科学逻辑与用于编排和执行计算的工作流引擎分离。工作流写成普通 Python 函数，可在多个受支持的工作流引擎上执行，而无须修改底层源代码，从而降低开发和贡献新工作流的门槛。QuAcc 还提供统一平台，以生成与目标模型一致的从头算参考计算，简化基础 MLIPs 的评估，并减轻评估模型性能时的方法学偏移。总之，这些特性使 QuAcc 成为一个灵活、易用的原子模拟工作流框架，服务于机器学习和人工智能日益重要的当下。

---

### 引言

计算化学与材料科学正处于一场数据革命之中，其动力来自人工智能（AI）的显著进展，以及持续推进材料设计与发现加速的努力。[1] 量子力学方法，例如基于密度泛函理论（DFT）的方法，在这些工作中发挥了核心作用，因为它们能够在广泛的化学体系和应用领域中预测物理化学性质。无数机器学习模型已被开发出来：它们或者以从头算的特征作为材料性质预测的输入，或者尝试直接预测从头算的结果。[2] 与此同时，基础机器学习原子间势（MLIPs）作为计算化学与材料科学的新范式出现，因为它们使研究者能够在仅靠从头算方法无法处理的时间与长度尺度上快速探索势能曲面。[3, 4] 虽然要实现加快材料设计和发现这一宏大目标仍有许多挑战需要克服，[5, 6] 量子力学模拟方法在当前的 AI 时代仍然不可或缺。

鉴于人们越来越广泛地依赖量子力学方法，迫切需要开源软件来提供高质量、可重现的模拟工作流，并以可扩展的工作流编排工具为基础。[7] 计算化学与材料科学群体也越来越具有跨学科特点，量子力学建模已不再仅由电子结构理论专家开展。因此，原子模拟软件必须使成熟方法易于使用，同时提供合理的默认设置以及避免错误计算的防护措施。[8] 随着用于构建和执行复杂科学工作流的代理式 AI 系统日益普及，这些要求变得比以往更加重要。[9-15] 即使对于人类用户，也不可能精通每一种量子力学模拟程序和材料建模任务；这凸显了可便捷扩展、由社区共同开发的软件库在执行复杂原子模拟工作流方面的价值。

就本文而言，我们将原子模拟中的计算基础设施分为三个不同层次：工作流引擎、原子模拟驱动程序和工作流库。这些类别并不总是互斥的，一些软件包提供跨越多个层次的功能。工作流引擎通常不针对特定领域，为定义、分派和监控复杂计算工作流提供抽象机制。目前已有超过 300 种工作流引擎被开发出来（尽管仍在积极维护的远少于此），[16] 而由于潜在最终用户的需求多样且相互冲突，恐怕永远不会有一种放之四海而皆准的方案。[17] 原子模拟驱动程序提供统一接口，以执行各种模拟软件包和常见类型的原子模拟任务。常见实例包括 Atomic Simulation Environment（ASE）、[18] 与 Custodian 配合使用的 Pymatgen，[19] 以及 TorchSim。[20] 最后，工作流库以工作流引擎和原子模拟驱动程序为基础，使用户易于执行、开发和共享复杂程度不同的计算化学与材料科学工作流。过去几年，已有多个面向计算材料科学工作流的软件包被开发出来，例如 Atomate2，[21, 22] 以及基于 AiiDA[23, 24] 和 Pyiron[25] 的软件包。大多数工作流库与单个工作流引擎紧密耦合；如果该引擎提供的功能与用户的计算需求不符，这种耦合便可能妨碍其采用。

本文介绍 Quantum Accelerator（图 1）的主要功能与设计理念，以下称为 QuAcc（发音为“quack”）。QuAcc 是一个用于原子模拟的工作流库，过去五年来一直以开放方式开发。它已被应用于化学与材料科学的多个领域，包括但不限于表面科学、分子反应性、固态材料热力学和超导性。[26-40] QuAcc 的一个核心设计目标，是将科学逻辑与执行该逻辑的工作流引擎解耦。QuAcc 中的原子模拟工作流写成普通 Python 函数，可在多个受支持的工作流引擎上执行，而无须重写底层源代码。因此，向 QuAcc 贡献或开发新工作流的门槛大为降低，因为开发者不必学习某种工作流语言的自定义语法及其众多细节。QuAcc 主要构建于社区广泛采用的 ASE 库之上，因此所有与 ASE 兼容的能量／力计算器都可使用。工作流引擎的互操作性与对原子模拟程序的广泛支持相结合，旨在使 QuAcc 无论面对最终用户何种计算需求都易于使用。

---

### 方法

原文没有独立的 Methods 章节；以下依原文顺序翻译承担方法说明功能的“Library of Simulation Recipes”“Architecture and Workflow Engine-Agnostic Design”和“Dependencies and Testing”三个章节。

#### 模拟配方库

QuAcc 提供多样化的预定义模拟“配方”库，涵盖第一性原理电子结构方法、半经验方法、经典原子间势和 MLIPs。在撰写本文时，已有针对多个电子结构软件包的受支持配方，包括 FHI-aims、[41] Gaussian、[42] MRCC、[43] ONETEP、[44] ORCA、[45] Psi4、[46] Q-Chem、[47] Quantum ESPRESSO[48, 49] 和 VASP。[50, 51] 这些接口共同提供分子和周期体系的 DFT（包括线性标度电子结构计算）及关联波函数方法。VASP 和 Q-Chem 配方还受益于 Custodian 库提供的额外功能；该库可对这两个程序的数十种常见错误进行自动处理。另有通过 DFTB+[52] 和 TBLite（包含 xTB 方法家族[53]）实现的半经验及紧束缚方法配方，以及通过 GULP[54] 实现的经典势配方，包括周期性 GFN-FF。[55]

为确保 QuAcc 与快速扩展的基础 MLIPs 生态系统保持兼容，该程序还可选择与若干外部库连接，包括 Rootstock、[56] matcalc[57] 和 FAIR-Chem。[58] 这些库通过 ASE 标准化地提供大量且持续发展的预训练模型。Rootstock 是 QuAcc 中特别有用的集成组件：用户可以借助它使用任何受支持的 MLIP 定义复杂工作流，而无须管理许多 MLIPs 所要求的相互冲突的 Python 环境。matcalc 和 FAIR-Chem 则提供另外的预训练基础 MLIPs 接入方式，但相关依赖的安装与管理由用户负责。QuAcc 还拥有一套独立的 TorchSim[20] 配方，供受益于在 GPU 上批量执行多个基于 MLIP 模拟的计算使用。

至少，每一种受支持的模拟程序都有静态计算和结构弛豫配方；不过，大多数程序还有更多配方，例如分子动力学、表面计算、振动频率和声子计算、过渡态搜索以及能带计算。为某种模拟程序添加新配方，只需开发者为相应任务类型定义一组合理的默认参数，并在适当情况下组合现有配方。该配方架构旨在随着新模拟方法和 MLIPs 的出现保持可扩展性。对于图 1 所示之外、基于 ASE 的计算器，只要定义适当的默认参数，即可方便地添加新配方。在所有情况下，ASE 都是写入相关输入文件并在适用时连接底层可执行程序的主要工具。在一些特定情况下（例如 Q-Chem、VASP），QuAcc 默认让 ASE 调用 Custodian。[19] Custodian 是一款可在运行过程中识别并纠正常见模拟错误的软件。在这些情况下，Custodian 管理任务执行，但输入文件写入与输出解析仍由 ASE 负责，以提供一致的用户体验。

QuAcc 中每个配方的输出都是一个字典，其中包含任务元数据和重要模拟结果的详细信息。我们把这些字典称为 schema。与工作流编排逻辑和基于 ASE 的计算器接口一样，QuAcc 不为底层科学模拟软件包提供自己的解析器。默认情况下，QuAcc 使用 ASE 写入所有输入文件，并从相应模拟输出文件读取关键性质（例如结构、能量、力和应力）。当已有成熟的文件解析器能够提供更丰富的（元）数据时，QuAcc 也会酌情采用。例如，所有基于 VASP 的 QuAcc 配方都建立在 Materials Project 所用的 schema 之上。[59]

#### 架构与不依赖特定工作流引擎的设计

QuAcc 不依赖特定工作流引擎的架构，使用户能够按自己的计算需求选择编排系统，而无须维护底层 QuAcc 源代码的不同版本。在撰写本文时，QuAcc 支持 Dask（包括与 dask-jobqueue 的集成）、[60] Jobflow（包括通过 Jobflow-Remote 和 FireWorks[61] 执行）、[62] Parsl、[63] Prefect、[64] Ray[65] 和 Redun[66] 工作流引擎；用户也可以完全不用工作流引擎，直接把配方作为普通 Python 函数运行。因此，QuAcc 工作流可在本地工作站、高性能计算集群和分布式云资源等多种环境中运行。这种不依赖特定引擎的架构还确保，即便某一工作流引擎停止维护——开源软件中常有这种情况——QuAcc 仍可继续工作。

虽然全面介绍每个受支持的工作流引擎超出了本文范围，但我们指出，每种选择都有其独特功能，可能影响最终用户的取舍。Dask、Parsl 和 Ray 针对高效任务执行而设计，使每秒向数百甚至数千个计算节点分派多达数千个任务成为可能；然而，与其他工作流引擎相比，这些程序缺乏详细的任务监控功能。Prefect 在数据工程界被广泛采用，具有强大的实时监控能力，包括用于监控大规模任务活动的可视化仪表板，但其内置的超级计算机复杂工作流监控支持有限。Jobflow 由 Materials Project 团队开发，面向学术超级计算机上的高通量模拟，严重依赖 MongoDB 等数据库。最后，Redun 主要用于在云计算资源上分派计算，尤其是基于 Amazon Web Services（AWS）的资源。

为了在工作流引擎之间实现高度互操作性，我们利用了许多现代 Python 工作流引擎中逐渐趋同的一种设计理念，即基于修饰器的编程模型。使用修饰器时，普通 Python 函数被转换成可独立执行的任务，而多个任务组成多步骤工作流（图 2）。虽然不同工作流引擎的底层执行细节、数据结构与调度机制有所不同，QuAcc 利用它们相似的语法，提供统一且不依赖特定引擎的接口。在 QuAcc 中，离散计算任务使用 `@job` 修饰器定义，工作流则使用 `@flow` 修饰器定义。QuAcc 还提供 `@subflow` 修饰器，用于表示更复杂的动态工作流模式：其中返回一组任务输出，但组成任务的数量可能无法事先确定。除了这些修饰器，底层 Python 函数的写法与常规函数相同。因此，配方的科学逻辑在很大程度上独立于执行它的编排框架。

导入经修饰的函数时，QuAcc 检查用户设置，以确定所选工作流引擎。随后，QuAcc 动态地把通用修饰器映射到该引擎提供的相应抽象机制。如果没有选择工作流引擎，这些修饰器便被忽略，函数保留普通的同步执行行为。这一设计理念允许先在本地开发和测试同一个配方，再通过分布式工作流系统部署，而无须修改源代码。QuAcc 将任务依赖管理、任务提交、监控和资源分配的所有方面交给所选的工作流引擎，本身不包含工作流逻辑。这种职责划分使科学配方与基础设施相关的编排逻辑解耦，并降低代码库的复杂性。

尽管受支持的工作流引擎语法相似，要实现图 2 所示的互操作性仍须解决几个挑战。考虑一个两步骤量子化学工作流：先进行结构弛豫，再进行静态计算；每个任务返回模拟结果字典，第二个任务访问第一个任务输出中的某个键。许多工作流引擎难以处理这种模式，因为字典的键只有在执行完成后才能解析，而等待这些键会削弱并发编程范式的优势。此外，工作流引擎在本地与远程机器之间传输任务时，对函数参数进行序列化和反序列化的方式不同，而且并非所有引擎都支持 Python 类以及 ASE Atoms 对象等领域特定抽象。解决这些限制既需要修改不同工作流引擎的上游代码库，也需要修改 QuAcc 代码库。

#### 依赖与测试

尽管支持大量模拟方法，为了确保 QuAcc 易于安装和使用，默认 Python 软件包仍只包含最少的一组依赖。另按用户可能感兴趣的配方定义了若干可选依赖组。整个代码库均配有单元测试和功能测试；在撰写本文时，QuAcc 的行覆盖率接近 100%。所有测试都可在本地运行，或由 GitHub Actions 自动运行；后者确保每个拉取请求都会运行核心测试套件。对于可通过 pip 或 Conda 软件包管理器方便安装的某些模拟程序，例如 DFTB+、Psi4 和 Quantum ESPRESSO，测试套件会执行真实但计算开销较低的电子结构计算。然而，对于无法作为 Python 包安装或属于专有软件的模拟程序，默认采用模拟执行。对于经过批准的用户和维护者，GitHub 上的拉取请求还会触发在本地计算集群上运行的专用测试套件，执行未经模拟的测试（例如针对 Gaussian、Q-Chem、VASP），以确保端到端流程持续可用。

---

### 结论

本文介绍 Quantum Accelerator（QuAcc）：一个用于原子模拟的开源工作流库，旨在使计算化学与材料建模工作流更易于使用、更可重现，并与各种工作流引擎互操作。QuAcc 提供广泛的预定义模拟配方，涵盖第一性原理电子结构方法、半经验与紧束缚方法、经典原子间势以及基础 MLIPs。QuAcc 主要以 ASE 为基础，并通过统一语法支持多个工作流引擎，从而把模拟工作流的科学逻辑与用于执行它的基础设施分离。这一设计允许相同的底层配方在本地、高性能计算资源或分布式环境中运行，而用户无须针对特定编排框架重写科学工作流。

除了简化常规原子模拟，QuAcc 还提供基础设施，以基于高通量计算构建可重现的数据集，并根据定义一致的从头算参考计算对基础 MLIPs 进行基准测试。其可扩展的配方架构、不依赖特定工作流引擎的设计，以及普通 Python 函数的使用，旨在降低复杂计算工作流的使用与开发门槛。随着原子模拟与机器学习和代理式 AI 系统越来越紧密地交织在一起，我们预计 QuAcc 这样的可互操作工作流库，将为把科学目标转化为可靠、可重现的计算提供重要基础。通过这种方式，QuAcc 旨在帮助人和机器更广泛地使用高质量原子模拟工作流，同时保持足够的灵活性，以伴随快速变化的计算化学与材料科学生态系统不断发展。

---

## 结果与讨论子标题翻译

原文没有名为“Results and Discussion”的总章节；与实例、基准测试和讨论相应的原文标题依出现顺序为：

- Representative Examples：代表性实例
- MLIP Training and Benchmarking：MLIP 训练与基准测试
- Outlook：展望

---

## 图表题翻译

图 1：Quantum Accelerator（QuAcc）及其组件概览。图中突出显示了 QuAcc 已有配方对应的模拟程序，以及当前支持的工作流引擎。

图 2：（a）由加法任务与随后执行的乘法任务构成的两步骤工作流有向图。（b–g）QuAcc 所支持的不同工作流引擎基于修饰器的语法。（h）对应的 QuAcc 修饰器；这些修饰器在导入时根据用户设置动态转换为对应工作流引擎的语法。

图 3：（a）自定义两步骤工作流的有向图，包括 GFN2-xTB 弛豫及随后的对应静态计算。（b）自定义两步骤工作流的有向图，包括使用 TensorNet-MatPES-PBE 机器学习原子间势进行结构弛豫，以及随后采用与 MatPES-PBE 兼容的设置执行静态密度泛函理论计算。（c）预定义动态工作流的有向图：生成不同的表面片，对每个表面片使用有效介质理论进行弛豫（仅为演示），然后进行对应的静态计算。

图 4：（a）使用 QuAcc 预定义配方生成与 MLIP 一致的 DFT 基准真值的工作流。（b）WBM 高能态数据集中 100 个结构的能量、力和应力误差的小提琴图。中间的虚线表示中位数，点线表示第一和第三四分位数。为使图示清晰，纵轴作了截断。

---

表 1：五个 MLIPs 相对于 WBM 高能态数据集原有 DFT 标签，以及通过 QuAcc 获得的、与相应 MLIP 兼容的 DFT 设置进行评估时，能量、力和应力的平均绝对误差（MAE）。

---

## 指定章节翻译

### 代表性实例

QuAcc 中的配方可以直接导入并使用，也可以组装成用户自定义的工作流。作为一个最简单的示例，我们首先考虑一个两步骤工作流：先对体相铜的 $2\times2\times2$ 超胞进行结构弛豫，再进行静态计算。我们使用 DFTB+ 程序[52]中实现的、带有周期性边界条件的 GFN2-xTB 方法[67]完成这两步计算（图 3a）。这里，我们导入两个预定义任务，并将它们串联起来，构成一个自定义工作流。其输出是一个字典，包含输入参数、更新后的 ASE Atoms 对象以及模拟的主要结果。默认情况下，工作流会作为标准 Python 代码运行；不过，通过 QuAcc 的设置管理器指定一个受支持的工作流引擎，同一段代码也可用于在远程计算机上分派该工作流。

在 QuAcc 中，不同类型模拟方法的配方也可以轻松组合。例如，图 3b 展示了这样一种计算：先使用在 MatPES-PBE 数据集[69]上训练的 TensorNet MLIP[68]进行弛豫，然后采用与 MatPES 兼容的设置，在 VASP 中进行静态计算。这可能用于评估经 MLIP 弛豫后的结构在能量、力和应力方面的误差。

除了预定义任务，QuAcc 还随附多个复杂程度不同的预定义工作流。作为一个代表性实例，图 3c 展示了一个动态工作流：它以体相结构为输入，切出高对称性表面片，对每个表面片进行结构弛豫，随后进行静态计算并汇集全部结果。在这里，我们选择使用有效介质理论（EMT），只是为了便于读者复现。由于各表面片的弛豫计算互不依赖，如果使用工作流引擎，并且有可用的计算资源，这些任务就会并发执行。

---

### MLIP 训练与基准测试

QuAcc 的众多用途之一是开发和评估大规模基础 MLIPs。评估预训练 MLIPs 对新材料或新应用领域的准确性时，能量（E）、力（F）以及适用时的应力（S）预测准确性至关重要。虽然 E/F/S 误差低并不能保证模型在目标下游模拟任务中也准确，但这是一个关键前提。评估预训练 MLIP 的 E/F/S 误差，通常需要对具有代表性的目标构型进行单点计算（即静态计算），然后比较 MLIP 与从头算参考结果给出的 E/F/S 预测。关键在于，从头算计算必须采用与训练该 MLIP 的数据相同的计算方法。理想情况下，这些计算应使用与原始数据集相同的电子结构程序、交换关联泛函、色散或 Hubbard U 修正（如适用），以及赝势或基组选择。上述任一设置的差异都可能引入显著的不一致，而这种不一致可能被错误地归因于 MLIP 的误差。

无论是专家还是非专家，都可能难以复现已发表的计算方案，特别是当重要的数值细节分散在论文、输入文件、软件代码仓库和补充材料中时。为了简化这一过程，QuAcc 提供预定义 DFT 配方，旨在复现多个广泛使用的 MLIP 数据集所采用的计算设置。这些数据集包括 Open Catalyst 2020、2022 和 2025（OC20、OC22、OC25），[70-72] Open Materials 2024（OMat24），[73] Open Molecular Crystals 2025（OMC25），[74] Open Molecules 2025（OMol25）和 Open Polymers 2026（OPoly26），[75, 76] Open Direct Air Capture 2023 和 2025（ODAC23、ODAC25），[77, 78] Materials Project Trajectory（MPtrj），[59, 79, 80] 抽样后的 Alexandria（sAlex），[73, 81] Materials Potential Energy Surface（MatPES），[69] 以及 Materials Project – Active Learning of Off Equilibrium structures（MP-ALOE）数据集。[82] 相同的配方既可用于构建内部一致的基准测试集，也可用于生成额外训练构型，以扩充已有数据集而不引入潜在的方法学不兼容。得益于 QuAcc 能够方便支持的高通量基础设施，用户还可以采用自己选择的设置以及任何受 ASE 支持的计算器，构建从头算训练数据。最后，我们指出，QuAcc 还提供若干配方，用以复现那些并非只用于 MLIP 训练的常见从头算数据集的设置，例如 Materials Project[59, 79] 和 Quantum Metal–Organic Framework（QMOF）Database。[83, 84]

为了演示，我们使用 QuAcc 对 WBM 高能态数据集[85]中的 100 个结构进行了单点 DFT 计算。该数据集是对 WBM 数据集[86]的结构在 1000 K 下进行分子动力学（MD）模拟得到的。这 100 个结构涵盖元素周期表中的 82 种元素；选择它们是为了尽可能提高元素的多样性，使我们能够考察不同元素之间的赝势差异，以及 Hubbard U 修正处理方式的差异，可能如何影响 E/F/S 误差。我们评估了五个 MLIPs：在 MatPES-PBE 数据集[69]上训练或微调的 TensorNet-MatPES-PBE (2025.2)[68, 69] 和 MACE-MatPES-PBE-0；[87] 以及在 OMat24 数据集[73]上训练或微调的 MACE-OMat-0 (medium)、PET-OMat-XL (v1.0.0)[88] 和 UMA-OMat-s1p2p1。[58] 我们将 MLIP 对能量、力和应力的预测，分别与 WBM 高能态数据集提供的单点 DFT 计算结果（即 MPRelaxSet 设置）以及通过 QuAcc 预定义配方实现的相应 MLIP 训练数据集设置下的计算结果进行比较。

如图 4 和表 1 所示，DFT 参考计算设置的选择对 MLIP 的表观准确性有显著影响。相对于 WBM 高能态数据集原有的 DFT 标签，基于 MatPES 训练的模型表现出很大的表观能量误差。相比之下，将同样的 MLIP 预测与完全兼容的 DFT 设置（即用于生成 MatPES 数据集的设置）进行比较，能量 MAE 降低了五倍。在基于 OMat24 数据集训练的 MLIPs 中也观察到类似趋势：将其预测与使用 QuAcc 按 OMat24 DFT 设置生成的基准真值标签比较时，能量 MAE 降至原来的一半以下。基于 MatPES 训练的 MLIPs 所表现出的特别大的能量差异，部分原因在于 MatPES 数据集不使用 Hubbard U 修正，而 OMat24 和 WBM 数据集都对特定材料组分使用 Hubbard U 修正。[89] DFT 设置的选择也影响力的 MAE：与 WBM 高能态数据集的 DFT 标签相比，改用完全一致的 DFT 设置评估后，五个模型的表观 MAE 均下降约 15–30%。相比之下，不同模型的应力误差变化较小，也不那么一致。我们注意到，WBM 高能态数据集中基于 MPRelaxSet 的 DFT 标签与 OMat24 数据集的标签都采用 $5.0\times10^{-5}$ eV/atom 的自洽场能量收敛准则；这可能影响数值收敛，特别是较大结构的晶胞应力。

这一实例的结果表明，用于评估 MLIPs 的 DFT 设置若不一致，会人为地放大 MLIP 误差。因此，要开展有意义的 MLIP 基准测试，单点 DFT 计算的基准真值标签必须采用与 MLIP 训练数据（或微调模型所用的微调数据集）相同的方法生成。QuAcc 的预定义配方便于使用内部一致的参考数据，对多个预训练 MLIPs 进行基准测试，从而使报告的误差更可靠地反映 MLIP 的性能，而不是底层 DFT 方法差异所造成的偏差。

---

### 展望

化学与材料建模领域的科学软件格局始终在演变，因此有必要思考该领域的现状，以及 QuAcc 这样的工作流库将来可能发挥的作用。科学界如今已发展到高通量计算成为常规手段的阶段；这在很大程度上得益于 QuAcc 等成熟工作流库，以及 Atomate2、[21] AiiDA[22, 23] 和 Pyiron[25] 等相关软件。与此同时，该领域正接近另一个转折点：大语言模型（LLMs）结合代理式 AI 方法，很可能在科学软件的开发和使用两方面发挥越来越重要的作用。这种转变为复杂化学与材料建模研究的自动化创造了新机会，但也对底层软件基础设施提出了新的要求。

广泛使用的 LLMs 在范围广泛的语料上训练，而这些语料未必体现高质量、由专家设计的计算方案。在这种背景下，QuAcc 这样的工作流库可以成为 AI 代理与底层模拟软件之间的重要一层。代理无须从头独立重建每项输入设置，而可以调用编码了合理默认设置和最佳实践的成熟配方。事实上，AI 编码代理平台 CatGo 已经通过导入 QuAcc 模板并以此为基础开展工作，展示了这一设想。[10] 随着代理式系统应用于异构计算环境，QuAcc 不依赖特定工作流引擎的设计也可能变得越来越重要。同一个工作流可以先在本地构建、检查和测试，再通过合适的工作流引擎分派到远程计算机，而无须重写代码本身。

我们预计，随着科学 AI 系统能力增强，QuAcc 这类工作流库的作用将扩大，而非减弱。基于 LLM 的代理可能越来越多地决定应开展哪些计算，用可组合的配方组装工作流，分析中间结果，并根据新发现调整后续计算。然而，领域专用的工作流库对于界定如何可靠地执行这些计算，并提供天然的防护机制，仍将不可或缺。因此，持续开发 QuAcc 这样开放、可互操作且由社区维护的工作流库，仍将十分重要；它有助于确保计算化学和材料科学中自动化程度的提高，同时伴随同样严格的可重现性、透明度和科学可靠性标准。
