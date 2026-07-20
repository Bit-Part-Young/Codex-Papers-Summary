# 文献总结 - exa-PD：用于多元素相图构建的可扩展高性能工作流 - 2026

## 文献基本信息

- 英文原文标题：exa-PD: A scalable high-performance workflow for multi-element phase diagram construction
- 中文标题翻译：exa-PD：用于多元素相图构建的可扩展高性能工作流
- 作者：Zhuo Ye, Feng Zhang, Maxim Moraru, Weiyi Xia, Ying Wai Li, Yongxin Yao, Cai-Zhuang Wang
- 作者单位：Ames National Laboratory, U.S. Department of Energy, Ames, Iowa 50011, USA；Los Alamos National Laboratory, Los Alamos, NM 87545, United States of America
- 发表期刊名称：文中未提供；该 PDF 为 arXiv 预印本格式。
- DOI 链接：文中未提供。
- 投稿 - 返修 - 接收 - 在线发表日期：文中未提供投稿、返修、接收日期；arXiv 版本信息为 arXiv:2607.15476v1 [cond-mat.mtrl-sci]，日期为 2026 年 7 月 16 日。
- 数据/代码链接：https://github.com/ML-AMD/exa-pd

## 文献总结

### 研究背景与需求

本文介绍了 exa-PD，一个用于构建多元素相图的高并行、高性能工作流。作者指出，计算材料发现随着计算能力和 AI/ML 技术的发展而快速推进，但实验验证仍然受限，其中一个重要原因是对可行合成路径的认识不足。因此，可靠的多元素相图对于理解合成条件下的热力学相竞争以及预测材料可合成性是必要的。

多元素相图的计算构建依赖高精度自由能计算。已有工作流已经为原子模拟中的自由能计算建立了稳健和高效的方法，但主要关注单个自由能计算的精度和效率。本文的 exa-PD 则面向另一个互补问题：如何以可扩展方式协调大量 MD/MC 任务，从而获得构建多元素相图所需的自由能数据。

### 工作流核心思想

exa-PD 使用 LAMMPS 中实现的分子动力学（MD）和蒙特卡罗（MC）标准采样技术，在精细的温度-成分网格上同时采样多个相，用于自由能计算。Parsl 作为全局工作流引擎，负责协调大量 MD 和 MC 任务，实现大规模并行与强可扩展性。随后，液相和固相的自由能结果输入 PyCalphad 进行 CALPHAD 建模，最终构建多元素相图。

本文展示的示例是 Cu-Zr 体系，图 1 给出了使用 EAM-FS 势由 exa-PD 预测的 Cu-Zr 相图。

### 技术路线

exa-PD 的工作流包括三个主要模块：

1. 固相自由能计算模块：以 Einstein 晶体等参考体系为基础，在某一温度下估算 Frenkel-Ladd 热力学积分，得到线性化合物等固相的自由能。之后通过升温或降温，并积分 Gibbs-Helmholtz 方程，获得其他温度下的自由能。
2. 液相自由能计算模块：以二元体系 $A_{1-x}B_x$ 为例，首先使用 Uhlenbeck-Ford 模型作为参考体系得到纯液体 $A$ 的自由能，然后通过 alchemical 热力学积分得到其他成分 $A_{1-x}B_x$ 的自由能。
3. 可选熔点计算模块：使用固-液共存（SLC）技术确定某一固相的熔化温度，用于验证自由能结果。

所有 MD 任务完成后，工作流通过 `run_process.py` 后处理结果。对于每个固相，该脚本生成 Gibbs 自由能 $G$ 随温度 $T$ 变化的两列数据集；对于液相，生成 $G(T,x)$ 的多列数据集，每一列对应一个不同成分。后处理还生成 TDB 格式的热力学数据库，包含所有计算过的固相和液相。示例脚本 `plot_PD.py` 可基于生成的 TDB 文件，使用 PyCalphad 可视化 Cu-Zr 相图。

### 并行化与异构资源支持

exa-PD 的执行模型依赖 Parsl 的动态任务分发。各模块包含多个异步任务，Parsl 将这些任务分配到可用计算资源上。许多 MD 任务可受益于 GPU 加速，但部分关键计算当前仍局限于 CPU，例如 Frenkel-Ladd 和 alchemical 热力学积分依赖的 LAMMPS 功能尚不受现有 GPU 或 KOKKOS 后端支持。

同时，作者指出，当使用 DeepMD 软件包中的预编译 LAMMPS 可执行文件来实现 DeepMD 神经网络势时，图 2 中展示的所有计算都可在 GPU 上高效执行。这使得工作流能够灵活利用异构 CPU/GPU 资源。

### 性能表现

作者在 NERSC 的 Perlmutter 超级计算机上，对 Cu-Zr 体系进行了 GPU 和 CPU 节点上的强扩展基准测试。图 3 总结了测试结果：随着计算节点数增加，GPU 和 CPU 的执行时间均接近理想线性扩展趋势。在最多 32 个节点的范围内，GPU 和 CPU 分别达到约 89% 和 90% 的并行效率。

### 输入结构支持

exa-PD 需要固相晶体结构作为自由能计算输入。它支持常见结构格式，包括 CIF 格式、VASP POSCAR 文件，以及扩展名为 `.lammps` 的标准 LAMMPS 输入文件。

### 论文贡献

本文的主要贡献在于提出并展示了一个面向多元素相图构建的可扩展工作流。它将 LAMMPS 中的 MD/MC 采样、Parsl 的全局并行任务调度、自由能后处理与 PyCalphad 的 CALPHAD 建模连接起来，形成从自由能计算到相图构建的自动化流程。该工作流尤其强调在大量相、温度和成分点上的任务依赖管理以及异构计算资源利用。

## 正文内容完整翻译

原文没有明确使用 “Abstract”“Introduction”“Methods”“Conclusion” 标题。本文将 `Summary` 视为摘要对应部分，`Statement of Need` 视为引言/研究需求对应部分，`Workflow Overview` 和 `Initial Crystal Structures` 视为方法对应部分。原文没有明确的 “Conclusion” 或 “Conclusions” 章节，因此无对应结论章节可逐字翻译。

### 摘要对应部分：Summary

exa-PD 是一种高度可并行化的工作流，设计用于构建多元素相图（PDs）[1]。它使用标准采样技术，即分子动力学（MD）和蒙特卡罗（MC），这些技术在 LAMMPS 软件包 [2] 中实现，用于在精细的温度-成分网格上同时采样多个相，以进行自由能计算。Parsl [3] 作为全局工作流引擎，协调大规模 MD 和 MC 任务集合，以实现具有强可扩展性的大规模并行化。随后，将所得液相和固相的自由能输入到通过 PyCalphad 软件包 [4] 进行的 CALPHAD 建模中，以构建多元素相图，如图 1 所示。

通过利用 Parsl 这一 Python 并行编程库，exa-PD 能够以可扩展方式执行大量带有内部任务依赖关系的 MD 和 MC 模拟集合，并可跨异构资源运行。该框架支持从单台工作站到多节点超级计算机的高效扩展，并且通过动态任务分发，在最高 32 个 GPU 上表现出近线性扩展，在最高 32 个 CPU 上也表现出良好扩展，如参考文献 [5] 的基准结果以及本文图 3 所示。

### 引言对应部分：Statement of Need

随着计算和 AI/ML 技术的进步，计算材料发现已经迅速发展。然而，实验验证仍然有限，这在很大程度上是由于对可行合成路径的认识不足。因此，可靠的多元素相图对于解析合成条件下的热力学相竞争以及预测可合成性至关重要。通过计算构建这些相图需要高度精确的自由能计算。传统工作流 [6] 已经建立了稳健且高效的自由能计算方法。它们主要关注单个自由能计算的准确性和效率。相比之下，exa-PD 解决的是一个互补挑战：对大量 MD/MC 作业进行可扩展协调，以获得多元素相图构建所需的自由能。使用 Parsl 实现全局控制器，确保了具有强可扩展性的大规模并行化，并能高效管理 MD/MC 作业，以处理资源密集型计算。通过将任务执行抽象为灵活的依赖图，Parsl 实现了一种数据驱动执行模型，在该模型中，任务会在其所需输入可用时立即被触发。虽然许多 MD 任务利用 GPU 加速，但某些必要功能仍然局限于 CPU 执行，因此需要异构 CPU/GPU 资源。Parsl 能够适应跨多种节点类型的这种异构执行，从而能够对用于自由能计算的 MD 模拟进行高通量管理。

### 方法对应部分：Workflow Overview

图 2 给出了 exa-PD 工作流的示意流程图，概述了构建相图所需的和可选的 MD/MC 作业，MD/MC 作业之间的内部依赖关系由橙色箭头表示。原则上，需要固相和液相的绝对自由能来生成相图。绝对自由能可以通过使用一个参考体系来获得，该参考体系的自由能可解析推导；然后通过热力学积分（TI）计算目标体系与参考体系之间的自由能差。该工作流的第一个模块通过使用某一温度下的参考体系（如 Einstein 晶体）并估算 Frenkel-Ladd TI，计算固相（线性化合物）的自由能。然后，它通过积分 Gibbs-Helmholtz 方程升高或降低温度，以获得其他温度下的自由能。第二个模块计算液体的自由能。以二元体系 $A_{1-x}B_x$ 为例，首先使用 Uhlenbeck-Ford 模型（UFM）作为参考体系获得纯液体 $A$ 的自由能，然后使用 alchemical TI 获得其他成分 $A_{1-x}B_x$ 的自由能。第三个模块是可选的，使用固-液共存（SLC）技术确定某一固相的熔化温度。SLC 模拟有助于验证自由能结果。

exa-PD 的执行模型依赖 Parsl 的动态任务分发。每个模块包括多个异步任务，Parsl 将这些任务分发到可用计算资源上。虽然许多 MD 任务受益于 GPU 加速，但一些必要计算目前仅限于 CPU 执行。例如，Frenkel-Ladd 和 alchemical TI 计算依赖于现有 GPU 或 KOKKOS 后端不支持的 LAMMPS 功能。然而，当使用 DeepMD 软件包中的预编译 LAMMPS 可执行文件来实现 DeepMD 神经网络势时，图 2 中展示的所有计算都可以在 GPU 上高效执行，从而能够灵活利用异构 CPU 和 GPU 资源。

图 3 总结了 Cu-Zr 体系的强扩展结果，该结果在 GPU 和 CPU 节点上均进行了评估。基准测试在国家能源研究科学计算中心（NERSC）的 Perlmutter 上进行。执行时间作为计算节点数的函数绘制，并同时给出理想线性扩展行为作为参考。GPU 和 CPU 结果在最高 32 个节点时都紧密跟随理想扩展趋势，并分别达到约 89% 和 90% 的并行效率。

此外，exa-PD 利用 Parsl 管理数百个 MD 任务之间的复杂依赖结构。例如，必须首先对固相进行平衡，以确定每个物种的平衡体积和均方位移（MSD），从而初始化 Frenkel-Ladd TI。这类任务依赖关系由 Parsl 控制器通过其基于 futures 的执行模型来表达和强制执行。

所有 MD 任务完成后，结果使用 `run_process.py` 脚本进行后处理。对于每个固相，该脚本生成 Gibbs 自由能 $G$ 作为温度 $T$ 函数的两列数据集。对于液相，它生成 $G(T,x)$ 的多列数据集，其中每一列对应一个不同成分。后处理步骤还生成 TDB 格式的热力学数据库，其中包含所有已计算固相和液相的条目。此外，还提供了示例脚本 `plot_PD.py`，用于基于生成的 TDB 文件，使用 PyCalphad 可视化 Cu-Zr 相图。

### 方法对应部分：Initial Crystal Structures

exa-PD 需要用于固相自由能计算的晶体结构作为输入。它接受以常用格式提供的晶胞结构，包括晶体学信息文件（CIF）格式和 Vienna Ab initio Simulation Package（VASP）POSCAR 文件 [7]。此外，exa-PD 支持扩展名为 `.lammps` 的标准 LAMMPS 输入文件。

### AI usage disclosure

生成式 AI 工具被用于协助语言润色和图形版式优化。所有技术内容均由作者审阅并验证。

### Acknowledgements

本工作得到了美国能源部（DOE）科学办公室基础能源科学、材料科学与工程部通过 Computational Material Science Center 项目的支持。Ames National Laboratory 由 Iowa State University 根据合同 DE-AC02-07CH11358 为美国 DOE 运营。Los Alamos National Laboratory 由 Triad National Security, LLC 根据美国能源部国家核安全管理局合同号 89233218CNA000001 运营。本研究使用了 NERSC 根据合同号 DE-AC02-05CH11231 提供的资源，以及 Los Alamos National Laboratory Institutional Computing Program 提供的资源。

## 结果/讨论章节子标题翻译

原文没有明确的 “Results” 或 “Discussion” 章节。正文中与结果或讨论相关的小节标题如下：

- 工作流概述
- 初始晶体结构

## 图题和表题翻译

图 1：使用 EAM-FS 势由 exa-PD 预测的 Cu-Zr 体系相图。

图 2：exa-PD 工作流的示意流程图。

图 3：exa-PD 工作流在 NERSC 的 Perlmutter 超级计算机上的强扩展。显示了 GPU 和 CPU 节点的挂钟时间。

本文正文中未见表格题注。
