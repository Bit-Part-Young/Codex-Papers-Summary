# 文献总结 - 高熵合金短程有序的可微逆向设计：从目标 SRO 到目标性能 - 2026

## 文献基本信息

- 英文原文标题：Differentiable Inverse Design of Short-Range Order in High-Entropy Alloys: From Target $\alpha$ to Target Property
- 中文标题翻译：高熵合金短程有序的可微逆向设计：从目标 $\alpha$ 到目标性能
- DOI 链接：https://doi.org/10.48550/arXiv.2607.02219
- 作者：Tiancheng Ding；Conrard Giresse Tetsassi Feugmo
- 机构：University of Waterloo, Department of Chemistry；University of Waterloo, Department of Physics and Astronomy
- 期刊 / 平台：arXiv 预印本，cond-mat.mtrl-sci；PDF 标注为 A PREPRINT。论文未给出正式期刊名称。
- 投稿 - 返修 - 接收 - 在线发表日期：arXiv 页面显示 Submitted on 2 Jul 2026；版本 v1 时间为 Thu, 2 Jul 2026 14:25:14 UTC。论文与 arXiv 页面未提供返修、接收或期刊在线发表日期。
- 数据 / 代码链接：https://github.com/feugmo-group/anisro
- 开源内容：论文 Data availability 声明中说明，`anisro` PyTorch 软件包、LAMMPS 输入文件、原子间势参数文件，以及用于训练性能替代模型的 LAMMPS-MEAM 弹性常数数据集均可在上述 GitHub 仓库获得；MEAM 势文件按其原始许可从 NIST Interatomic Potentials Repository 再分发。
- 本总结依据：用户提供的 PDF、arXiv 页面 https://arxiv.org/abs/2607.02219、arXiv TeX 源文件和论文 Data availability 声明。

---

## 文献总结

### 研究对象与核心问题

这篇论文围绕多主元合金和高熵合金中的化学短程有序（SRO）开展。作者指出，Warren-Cowley 参数 $\alpha_{ij}^{(r)}$ 不只是热力学描述符，而是可以直接作为合金设计变量：它影响局域键合拓扑，并进一步影响广义层错能曲面、位错芯宽度、孪生应力和氢陷获环境。

论文要解决的是一条完整的逆向设计链：从目标 SRO 签名出发，生成匹配该 SRO 的原子构型，再进一步面向目标弹性性能进行结构设计。作者认为传统流程中 ARMC、性能预测和结构验证是分离的离散阶段，不能共享梯度，因此难以形成端到端可微的性能设计循环。

### 方法框架

作者提出 ANISRO，这是一个端到端可微的 PyTorch 框架。其主要组成包括：

1. 前向 NIMM 求解器：将 Rao 和 Curtin 的 Non-Interacting Molecule Method 从二元推广到 $K$ 组元，输入有效对相互作用 $\{V_{ij}^{(r)}\}$、成分 $\{c_i\}$ 和温度 $T$，输出平衡 Warren-Cowley 参数 $\{\alpha_{ij}^{(r)}\}$。
2. 可微 Warren-Cowley 计数器：用每个晶格位点的软占据概率 $P \in [0,1]^{N\times K}$ 表示构型，并通过 softmax logit 场 $\boldsymbol{\ell}$ 参数化，使 $\alpha$ 的统计计数可以对 $\boldsymbol{\ell}$ 自动求导。
3. 梯度式 SRO 到结构逆设计：以 $\sum(\hat{\alpha}-\alpha^\star)^2$ 为核心损失，并加入成分、二值化熵和可选的 NIMM 自由能正则化项，用 Adam 优化，再通过逐组元 top-$k$ 投影生成硬的 LAMMPS 构型。
4. 性能替代模型：用成分、多壳层 $\alpha$ 和占据方差作为描述符，训练 $d$-64-64-1 的 MLP 预测 LAMMPS-MEAM 弹性常数。
5. 闭环性能设计：将目标性能误差反向传播到 logit 场，从而在一次自动微分链路中完成从目标 $C_{11}$ 到原子构型的优化。

### 主要结果

在 Cu-Ni 的前向验证中，作者将 $K$ 组元 NIMM Newton 求解器的 $\alpha^{(1)}$ 与 Metropolis Monte Carlo 结果比较。在 Rao 和 Curtin 给出的对簇有效区间 $0.5 < x^{(1)} < 1.5$ 内，NIMM 和 MC 在所有网格点上符号一致，并且误差满足 $|\Delta \alpha| < 0.03$。

在 SRO 到结构的逆设计基准中，256 原子 Cu-Ni 小胞上 ARMC 仍有更低残差；但在 4000 原子 Co-Cr-Ni 超胞中，ARMC 在约 7 min 内最大逐对 $\alpha$ 误差达到 0.439，而梯度方法在 71 s 内达到 0.054。论文据此报告，在 4000 原子规模上梯度方法比 ARMC 快 $6\times$，且精度高 $8\times$。

在 9 个 FCC/BCC 合金体系的调查中，作者用真实 LAMMPS-MEAM 弹性常数比较梯度设计构型与随机参照构型。论文报告的 SRO 诱导 $C_{11}$ 变化范围从 Cr-Cu-Ni 的 $-20\,\%$ 到 Cr-Fe-Ni 的 $+57\,\%$。作者特别指出，这些 108 原子调查小胞结果应理解为单胞指标而非收敛热力学平均；后续尺寸验证显示，$3\times3\times3$ 到 $6\times6\times6$ 超胞范围内 $\Delta C_{11}$ 的符号和大小都对尺寸敏感。

在 Co-Cr-Ni 闭环性能设计中，作者用 50 个 $\alpha$ 目标与真实 LAMMPS 弹性常数训练描述符 MLP。虽然 $C_{11}$ 验证集 $R^2$ 出现过拟合，但闭环设计的 4 个目标中有 3 个经独立 LAMMPS-MEAM 验证后落在目标值 6 % 以内；240 GPa 目标偏离较大，被作者归因于替代模型外推区间泛化不足。

### 论文中的限制与作者给出的解释

作者强调 NIMM 自由能正则化项继承了对簇模型的有效区间，即 $0.5 < x_{ij}^{(r)} < 1.5$，或等价地 $|V_{ij}^{(r)}| \lesssim 0.7\,k_BT$。部分 2NN-MEAM 势在 300 K 给出的异质对 EPI 超出该范围，例如 CoCrNi 的 $V_{\rm CoCr}\approx0.11$ eV；在这些情况下，解析 NIMM 会低估 MC $\alpha$ 的幅值但保持符号。因此论文将 NIMM 用作软的物理先验，而不是硬约束。

作者还指出，原子间势选择会影响 SRO  motif 的符号和强度。以 Cantor 合金为例，LAMMPS-MEAM 和 MACE-MP-0 在若干 SRO motif 的符号上存在差异。论文把这种差异视为势函数化学描述差别的诊断，而不是框架本身的错误。

---

## 章节翻译
### 摘要

短程有序（SRO）支配多主元合金的力学响应，然而，从目标 Warren-Cowley 签名到原子构型，并进一步到目标性能的逆向设计，通常在彼此断开的阶段中求解，而这些阶段不能共享梯度。我们用连续占据晶格上的端到端梯度下降取代随机的原子级反向 Monte Carlo（ARMC），并将其连接到一个在真实原子间势弹性常数上训练的可微性能替代模型。本文报告 3 项贡献：（1）基于梯度的 SRO 到结构反演在小胞尺寸上达到 ARMC 的精度，在 4000 原子超胞上快 $6\times$ 且精度高 $8\times$，并且平滑扩展到 $K$ 个组元而不需要逐移动记账；（2）一个从 Rao 和 Curtin 的 Non-Interacting Molecule Method（NIMM）导出的热力学正则化项，在此从二元推广到 $K$ 组元，将设计构型锚定到所选有效对相互作用的自由能曲面上，从而去除统计上有效但物理上不一致的解；（3）一个在成分、多壳层 $\alpha$ 和占据统计量上训练的描述符多层感知机驱动闭环性能设计：该流程应用于 9 个面心立方（FCC）和体心立方（BCC）合金体系的调查，在 108 原子调查小胞中恢复了 SRO 诱导的 $C_{11}$ 变化，其范围从 $-20\,\%$（Cr-Cu-Ni）到 $+57\,\%$（Cr-Fe-Ni），并且通过胞尺寸验证（$3\times3\times3$ 到 $6\times6\times6$）显示，$\Delta C_{11}$ 的符号和大小在低于 864 原子时尚未收敛；此外，该流程在 Co-Cr-Ni 的真实 LAMMPS 改进嵌入原子方法（MEAM）弹性常数上闭合了设计循环，4 个目标 $C_{11}$ 值中有 3 个位于 6 % 以内。该框架作为开源 PyTorch 软件包 `anisro` 发布，并为浓缩固溶体中的基于梯度的性能设计提供了一条路径。

关键词：高熵合金；短程有序；逆向设计；可微编程；弹性常数

### 引言

化学短程有序（SRO）正在成为浓缩固溶体和高熵合金（HEA）中一种可控的设计变量 [7,17,28,46]。Warren-Cowley 参数 $\alpha_{ij}^{(r)}$ 是一种相对于随机合金衡量第 $r$ 配位壳层中异质对富集程度的带符号量，它设定了局域键合拓扑，并通过该拓扑设定广义层错能曲面、位错芯宽度、孪生应力和氢陷获环境。在典型的 Cr-Co-Ni 中熵合金中，原子探针层析和电子衍射实验揭示了纳米尺度的有序畴，这些有序畴与层错能 15-20 % 的变化以及变形机制从位错滑移到纳米孪晶的转变相关 [14,47,48]。随后跨越面心和体心化学体系的研究已经将 SRO 与屈服强度、加工硬化能力、抗氢脆性能和抗辐照性能联系起来 [8-10,25,43,45]。对于合金设计者而言，其含义是具体的：$\alpha_{ij}^{(r)}$ 不再只是一个热力学描述符，而是一个目标变量；如果其数值能够在实验室或模拟中实现，它就可以预测合金的力学签名。

连接 SRO 与弹性响应的微观机制经过局域力常数环境。负的 $\alpha_{ij}^{(r)}$ 表示壳层 $r$ 中异质对富集：组元 $i$ 的配位壳层中包含的 $j$ 近邻多于相同成分随机合金中的数量。当 $i$-$j$ 键比 $i$-$i$ 或 $j$-$j$ 替代键更硬时，例如 Cr-Fe-Ni 体系中的 Cr-Fe 对，这种富集会提高有效原子间力常数并使晶体硬化，表现为 $C_{11}$ 增大。相反，当异质对更软或通过尺寸失配引入晶格应变时，例如 Co-Cr-Ni 中的 Co-Cr 对，有序化会使晶体软化并降低 $C_{11}$。定量幅值取决于组元之间的键刚度差异、壳层配位几何以及有序程度：即使是适中的 $|\alpha|\sim0.3$-0.4 数值，也完全位于对簇有效区间内，并且可以使弹性模量移动数十 GPa。

量化和设定 SRO 所需的计算工具已经迅速成熟。在前向方面，密度泛函理论结合正则 Monte Carlo 仍然是小超胞和短轨迹的参考 [16,27,38]；在 DFT 数据上训练的机器学习原子间势（MLIP）把可访问的体系尺寸扩展到几十万原子 [5,13,19,22,26,29]；Rao 和 Curtin 的解析 Non-Interacting Molecule Method（NIMM）[31] 通过廉价的 Newton 求解，从少量有效对相互作用（EPI）给出闭式 Warren-Cowley 参数，并且有明确的有效区间。在逆向方面，生成统计 $\alpha$ 与规定目标元组匹配的原子构型时，原子级反向 Monte Carlo（ARMC）是事实标准，Sheriff 及合作者的最新工作为多组元体系建立了最佳实践 [20,36,37]。

尽管这些单独进展已经存在，从目标 $\alpha$ 到目标力学性能的链条仍然由不能交换梯度的离散阶段拼接而成。ARMC 产生与目标 $\alpha$ 一致的构型，但不提供关于该目标或底层 EPI 的平滑梯度；将其输出耦合到性能预测器并向后传播敏感性，需要无导数外循环或分段重新训练。与此同时，更广泛的可微分子模拟共同体已经展示了当正向和逆向算子被写成可组合、自动可微程序时可以实现什么：端到端能量最小化、NVT 采样和力场优化都已经在 JAX 或 PyTorch 中得到展示 [1,4,15,18,30,35]。据我们所知，对于 HEA 中 SRO 到结构再到性能的问题，尚不存在等价的端到端可微表述。

我们弥合这一缺口。核心技术动作是把 Warren-Cowley 计数器本身写成纯函数式、完全可微的张量操作，该操作作用于连续的逐位点组元概率 $P \in [0,1]^{N\times K}$，并通过 softmax 由自由 logit $\boldsymbol{\ell}$ 参数化。在这一表示下，$\boldsymbol{\ell}$ 上的梯度下降最小化与 ARMC 通过随机交换移动所最小化的同一个 $\sum(\hat{\alpha}-\alpha^\star)^2$ 残差，同时还尊重成分、二元熵和热力学正则化项。热力学正则化项是 NIMM 自由能的可微重写，并推广到 $K$ 组元；它把设计构型锚定到所选 EPI 的自由能曲面上，并移除统计上有效但物理上不一致的解。相同的 logit 参数化扩展到性能设计：用替代性能预测替代 SRO 损失，通过单次反向传播把目标力学性能连接到原子构型。

本文报告 3 项贡献。梯度 SRO 到结构反演在小型二元晶胞上达到 ARMC 精度，并且在 4000 原子超胞上快 $6\times$、精度高 $8\times$，由于每步成本与组元数无关，因此可平滑扩展到 $K$ 个组元。按照 Rao 和 Curtin [32] 从二元推广到 $K$ 组元的 NIMM 衍生自由能正则化项，使设计构型与所选 EPI 曲面保持物理一致，而不仅仅是在统计上匹配 $\alpha$。在真实 LAMMPS-MEAM 弹性常数上训练的描述符多层感知机驱动 Co-Cr-Ni 的闭环性能设计，并在 9 个 FCC/BCC 体系调查中恢复了范围从 $-20\,\%$（Cr-Cu-Ni）到 $+57\,\%$（Cr-Fe-Ni）的 SRO 诱导 $C_{11}$ 变化。完整流程见图 4。该框架作为开源 PyTorch 软件包 `anisro` 发布。

---

### 方法

图 1 提供了 ANISRO 框架的高层概览；包含全部 4 个阶段且用颜色编码的完整流程，在本节末尾的图 4 中汇总。

#### 2.1 Warren-Cowley 短程有序参数

全文采用 Warren-Cowley 约定 [12,42]。对于具有 $N$ 个位点和 $K$ 个组元的晶格，以及配位数为 $z_r$ 的第 $r$ 配位壳层，联合对概率 $P_{ij}^{(r)}$ 是组元 $i$ 的位点在壳层 $r$ 中具有组元 $j$ 近邻的概率。Warren-Cowley 参数为

$$
\alpha_{ij}^{(r)} = 1 - \frac{P_{ij}^{(r)}}{c_j},
$$

其中 $c_j$ 是组元 $j$ 的全局摩尔分数。$\alpha_{ij}^{(r)} < 0$ 表示 $i$ 周围 $j$ 的富集（有序倾向）；$\alpha_{ij}^{(r)} > 0$ 表示耗尽（团簇化或相分离倾向）。对于随机合金，所有对和壳层都有 $\alpha_{ij}^{(r)} = 0$。矩阵 $\boldsymbol{\alpha}^{(r)} \in \mathbb{R}^{K\times K}$ 是对称的（$\alpha_{ij}^{(r)} = \alpha_{ji}^{(r)}$），并且对每个 $i$ 满足线性约束 $\sum_j c_j \alpha_{ij}^{(r)} = 0$，因此每个壳层留下 $K(K-1)/2$ 个独立的异质对参数。

#### 2.2 $K$ 组元的前向 NIMM 求解器

前向算子将逐壳层异质对有效对相互作用（EPI）表 $\{V_{ij}^{(r)}\}$、成分 $\{c_i\}$ 和温度 $T$ 映射到 Warren-Cowley 矩阵 $\{\alpha_{ij}^{(r)}\}$。EPI 在形成能约定中定义为

$$
V_{ij}^{(r)} = U_{ii}^{(r)} + U_{jj}^{(r)} - 2 U_{ij}^{(r)},
$$

其中 $U_{ij}^{(r)}$ 是壳层 $r$ 上完全有序的 $ij$ 最近邻环境的逐位点键能。正的 $V_{ij}^{(r)}$ 相对于对称平均降低 $ij$ 键的能量，从而驱动有序化（$\alpha_{ij} < 0$）；负的 $V_{ij}^{(r)}$ 促进团簇化（$\alpha_{ij} > 0$）。

我们从 Rao 和 Curtin 的 Non-Interacting Molecule Method [31] 出发，并将他们的二元推导推广到 $K$ 个组元。对于每个配位壳层 $r$，对簇的构型状态是 $K$ 个同质类别 $(i,i)$ 之一，其简并度 $g_k = 1$；以及 $K(K-1)/2$ 个异质类别 $(i,j)$、$i < j$，其简并度 $g_k = 2$；因此总共有 $K_r = K(K+1)/2$ 个簇类别。定义无量纲对逸度

$$
x_{ij}^{(r)} = \exp\!\left(\frac{-V_{ij}^{(r)}}{k_B T}\right),
\qquad x_{ii}^{(r)} = 1,
$$

在质量平衡约束下最大化簇占据熵所得的变分驻定条件给出逐簇对数概率：

$$
\ln p_k^{(r)} = \ln g_k
        - \frac{1}{2}\sum_{i,j} N_{ij,k}^{(r)}\ln x_{ij}^{(r)}
        + \sum_i \lambda_i\!\left(2 N_{ii,k}^{(r)} + \sum_{j\neq i} N_{ij,k}^{(r)}\right)
        + \mu,
$$

其中 $N_{ij,k}^{(r)} \in \{0,1\}$ 是簇类别 $k$ 中对 $(i,j)$ 的重数，Lagrange 乘子 $\{\lambda_i\}$ 施加 $K$ 个质量平衡约束

$$
2\sum_k p_k N_{ii,k}^{(r)} + \sum_{j\neq i}\sum_k p_k N_{ij,k}^{(r)} = 2c_i
  \quad \forall\, i,
$$

而 $\mu$ 施加 $\sum_k p_k = 1$。对逸度项 $-\tfrac{1}{2}\sum_{ij} N_{ij,k} \ln x_{ij}$ 的符号与来自 Stirling 链式法则的 $-1$ 结合，在最终驻定方程中产生 $-\ln x_{ij}/2$，因此正的 $V_{ij}$（正的 $\ln x_{ij}$）会提高异质对类别的 $\ln p_k$，并驱动 $\alpha_{ij} < 0$。这一符号约定在第 3.1 节中得到数值验证，并在补充信息 S1 节中作形式推导。

$K_r + K + 1$ 个非线性方程按壳层逐一用带阻尼的 Newton 迭代求解，并使用列重标度 Jacobian：

$$
\mathbf{J}\,\delta\mathbf{x} = -\mathbf{r},\qquad
\mathbf{J}_{kl} = \frac{\partial r_k}{\partial x_l},
$$

其中残差 $\mathbf{r}$ 收集驻定方程、质量平衡约束和归一化约束。Armijo 线搜索在整个迭代过程中保持每个 $p_k > 0$。在本文所有体系中，包括五组元 Cantor 合金（$K_r = 15$），Newton 残差都在少于 30 次迭代内达到机器精度（$\|\mathbf{r}\| < 10^{-14}$）。包含伪代码和收敛数据的完整算法见补充信息 S1.2 节。

联合对概率和 Warren-Cowley 参数由下式给出：

$$
P_{ij}^{(r)} = \sum_k p_k^{(r)}\, N_{ij,k}^{(r)} / N_r,
$$

$$
\alpha_{ij}^{(r)} = 1 - P_{ij}^{(r)} / (2 c_i c_j),
$$

这与 Rao 和 Curtin 的式（12）和式（13）相匹配。这里 $P_{ij}^{(r)}$ 计数对称对（包括 $(i,j)$ 和 $(j,i)$ 两个方向），所以随机合金中 $P_{ij}^{(r)} = 2c_ic_j$，从而与上面的 Warren-Cowley 定义一致地恢复 $\alpha_{ij}^{(r)}=0$；这与该定义中使用的单方向条件概率相差因子 $2c_i$。该求解器在 PyTorch 中实现（`anisro.forward.pair_cluster`），因此其输出仍可通过 EPI 表和成分求导，从而支持基于梯度的 EPI 回归。

NIMM 模型在对簇有效区间 $0.5 < x_{ij}^{(r)} < 1.5$ 内定量可靠，等价地 $|V_{ij}^{(r)}| \lesssim 0.7\,k_BT$，这一点由 Rao 和 Curtin 划定。本文研究的若干专用 2NN-MEAM 在 300 K 产生的 EPI 违反该界限；在这些情况下，梯度逆设计直接以 Metropolis MC $\alpha$ 为目标，仅将 NIMM 用作软先验，而不是硬约束。

#### 2.3 可微 Warren-Cowley 计数器

对于逆问题，原子构型由软占据张量 $P \in [0,1]^{N \times K}$ 参数化，并且对每个位点 $n$ 有 $\sum_i P_{ni} = 1$（这不同于第 2.1 节中的联合对概率 $P_{ij}^{(r)}$；二者由上下文区分），该张量从自由 logit 矩阵 $\boldsymbol{\ell} \in \mathbb{R}^{N \times K}$ 通过逐行 softmax 得到：

$$
P_{ni} = \frac{\exp(\ell_{ni})}{\sum_{i'}\exp(\ell_{ni'})}.
$$

当 $\boldsymbol{\ell}$ 高度尖锐时，$P$ 接近 one-hot 矩阵（整数占据）；$\boldsymbol{\ell}$ 上的梯度下降探索离散组合空间的连续松弛。图 2 展示了这种参数化以及硬投影步骤。

给定壳层邻接矩阵 $A^{(r)} \in \{0,1\}^{N \times N}$，且对每个位点 $n$ 都有 $\sum_m A^{(r)}_{nm} = z_r$，壳层 $r$ 中 $(i,j)$ 对的数量为

$$
\mathrm{num}_{ij}^{(r)} = \sum_{n,m} P_{ni}\, A^{(r)}_{nm}\, P_{mj}
                          \equiv \texttt{einsum(`ni,rnm,mj->rij', P, A, P)},
$$

组元 $i$ 的软成分为 $n_i = \sum_n P_{ni}$、$c_i = n_i/N$，可微 Warren-Cowley 参数为

$$
\hat{\alpha}_{ij}^{(r)}(P) = 1 - \frac{\mathrm{num}_{ij}^{(r)}}{z_r\, n_i\, c_j}.
$$

当 $P$ 为 one-hot 时，该表达式是精确的，并退化为 ARMC 使用的离散统计计数器；对于任意 $P \in [0,1]^{N\times K}$，该表达式都是平滑的。上述 `einsum` 原样携带一个可选的前导 batch 维度，使计数器与 `torch.func.vmap` 兼容，从而可在多个目标 $\alpha$ 元组上并行。

#### 2.4 梯度 SRO 到结构逆设计

逆向目标最小化软构型的 SRO 与目标矩阵 $\boldsymbol{\alpha}^\star$ 之间的偏差。SRO 损失是在观测到的异质对集合 $\Omega$ 上、按壳层加权并带掩码的均方误差：

$$
\mathcal{L}_{\alpha}(\boldsymbol{\ell}) =
  \sum_{r}\, w_r \sum_{(i,j)\in\Omega}
  \bigl(\hat{\alpha}_{ij}^{(r)}(P(\boldsymbol{\ell})) - \alpha_{ij}^{\star\,(r)}\bigr)^{2}.
$$

两个正则化项吸收 ARMC 通过其移动设计隐式施加的硬约束：

$$
\mathcal{L}_{\rm comp}(\boldsymbol{\ell})
    = \sum_{i=1}^{K}\!\left(\overline{P}_i - c_i^{\star}\right)^{2},\quad
     \overline{P}_i = \frac{1}{N}\sum_n P_{ni},
$$

$$
\mathcal{L}_{\rm bin}(\boldsymbol{\ell})
    = -\frac{1}{NK}\sum_{n,i} P_{ni}\ln P_{ni}.
$$

成分损失 $\mathcal{L}_{\rm comp}$ 驱动每个组元的平均占据接近目标摩尔分数；二值化损失 $\mathcal{L}_{\rm bin}$ 是逐位点熵，它在均匀 $P_{ni} = 1/K$ 时最大，并在 one-hot $P$ 时最小（为零）；因此最小化 $-\mathcal{L}_{\rm bin}$ 会把每个位点拉向明确的组元赋值。总损失为

$$
\mathcal{L}_{\rm total}
    = \lambda_\alpha\,\mathcal{L}_\alpha
    + \lambda_{\rm comp}\,\mathcal{L}_{\rm comp}
    + \lambda_{\rm bin}\,\mathcal{L}_{\rm bin}
    + \lambda_{\rm phys}\,\mathcal{L}_{\rm phys},
$$

其中 $\mathcal{L}_{\rm phys}$ 是可选的 NIMM 自由能正则化项。全文使用的默认权重为：$\lambda_\alpha = 1$、$\lambda_{\rm comp} = 5$、$\lambda_{\rm bin} = 0.01$、$\lambda_{\rm phys} = 0$（梯度逆设计）或 0.1（混合方法）。

优化使用 PyTorch [30] 中的 Adam [21]，学习率为 $10^{-2}$，$(\beta_1,\beta_2) = (0.9, 0.999)$，并将 logit 裁剪到 $[-10, 10]$。在 $N_{\rm steps} = 1500$ 步之后，通过逐组元 top-$k$ 选择把最佳损失快照投影为硬构型：对于每个组元 $i$，将 $P_{ni}$ 最高的 $\lfloor c_i^\star N \rfloor$ 个位点赋为组元 $i$。这一投影会在 $\alpha$ 中引入软到硬漂移；我们同时报告优化末端的软 $\hat{\alpha}$ 和由离散计数器在投影构型上计算的硬 $\alpha$。完整的逐组元 top-$k$ 算法见补充信息 S3 节。

#### 2.5 NIMM 自由能正则化项

为了使梯度逆设计偏向于在所选 EPI 下热力学上可信的构型，而不仅仅是在统计上匹配目标 $\alpha$，我们加入 NIMM Helmholtz 逐原子自由能的可微近似。将 Rao 和 Curtin 的式（22）推广到 $K$ 组元和固定成分，对每个配位壳层 $r$ 有

$$
\frac{F^{(r)}}{N} =
  -\frac{z_r}{4}\sum_{i \neq j} \tilde{P}_{ij}^{(r)}\, V_{ij}^{(r)}
  +
  \frac{k_B T\, z_r}{4}\sum_{i,j} \tilde{P}_{ij}^{(r)}\ln \tilde{P}_{ij}^{(r)},
$$

其中 $\tilde{P}_{ij}^{(r)} = \mathrm{num}_{ij}^{(r)} / (z_r n_i)$ 是通过用预期的 $i$ 类型键数归一化 $\mathrm{num}_{ij}^{(r)}$ 得到的联合对概率。第一项是平均对能（仅含异质对贡献；在固定成分下同质对能量从变分问题中消去）；第二项是构型熵，即 $-TS$。对能项前的负号遵循 EPI 符号约定：当 $V_{ij} > 0$ 时，最小化 $F^{(r)}$ 会增加 $\tilde{P}_{ij}^{(r)}$（更多异质对），这与前向 Newton 求解器预测的平衡相同。

物理正则化项为 $\mathcal{L}_{\rm phys} = \sum_r F^{(r)}/N$，其关于 $\boldsymbol{\ell}$ 的梯度由 PyTorch autograd 通过上述 softmax 到 NIMM 自由能方程计算。当 $\lambda_{\rm phys} > 0$ 时，优化器最小化组合的 SRO + 热力学损失，使构型同时匹配 $\alpha^\star$ 并位于所选势的自由能极小附近。

#### 2.6 性能描述符和替代模型

描述符向量 $\boldsymbol{d}(P)$ 串联了 4 组直接从软占据张量计算的特征：

$$
\boldsymbol{d}(P) = \Bigl[
    \underbrace{c_1,\ldots,c_K}_{\rm composition},\;
    \underbrace{\hat{\alpha}_{ij}^{(1)}}_{\rm 1NN\;SRO},\;
    \underbrace{\hat{\alpha}_{ij}^{(2)}}_{\rm 2NN\;SRO},\;
    \underbrace{\sigma^2_{\rm occ,\,i}}_{\rm occupancy\;var.}
  \Bigr] \in \mathbb{R}^{d},
$$

其中 $\sigma^2_{{\rm occ},i} = \tfrac{1}{N}\sum_n (P_{ni} - c_i)^2$ 衡量逐组元占据方差（对于良好偏聚的 SRO 较大，对于弥散占据较小）。对于 $K$ 组元、2 壳层体系，$d = K + K(K-1) + K = K(K+1) = 12$，当 $K = 3$ 时如此。

替代模型 $\phi_\theta : \mathbb{R}^d \to \mathbb{R}$ 是一个双隐藏层多层感知机（MLP），架构为 $d$-64-64-1，带层归一化和 ReLU 激活。它通过最小化预测值与一批梯度设计构型上的 LAMMPS-MEAM 弹性常数之间的均方误差来训练，采用 80/20 训练-验证划分，并在 50 个 epoch 无改进时早停。由于 $\phi_\theta$ 和 $\boldsymbol{d}(P)$ 都可对 $\boldsymbol{\ell}$ 求导，梯度 $\partial \phi_\theta / \partial \boldsymbol{\ell}$ 可通过自动微分以无额外成本获得。从 logit 场经由描述符构建到替代模型预测和反向传播的完整数据流总结在图 3 中：顶行显示推断路径，虚线底行显示训练路径，节点上方的红色路径表示梯度端到端流向 logit 场，并驱动第 2.7 节的闭环设计。

#### 2.7 闭环性能设计

给定目标性能值 $y^\star$ 和训练好的替代模型 $\phi_\theta$，闭环设计问题用性能损失替代 SRO 损失：

$$
\mathcal{L}_{\rm prop}(\boldsymbol{\ell})
    = \bigl(\phi_\theta(\boldsymbol{d}(P(\boldsymbol{\ell}))) - y^\star\bigr)^2
    + \lambda_{\rm comp}\,\mathcal{L}_{\rm comp}
    + \lambda_{\rm bin}\,\mathcal{L}_{\rm bin}.
$$

梯度 $\nabla_{\boldsymbol{\ell}}\mathcal{L}_{\rm prop}$ 在一次反向传播中通过替代模型、描述符、可微 $\alpha$ 计数器和 softmax 计算。不需要有限差分 Jacobian 或单独的伴随求解。优化使用与 SRO 逆设计相同的 Adam 调度器，在 1500 步（约 0.8 s）内收敛。最终硬构型通过独立的 LAMMPS-MEAM 弹性常数运行进行评估，以验证替代模型预测可迁移到真实势。

#### 2.8 原子级反向 Monte Carlo 基线

原子级反向 Monte Carlo（ARMC）是我们的随机基线。从目标成分的随机构型 [49] 开始，ARMC 提出随机的成对组元交换，其接受由 Metropolis 判据 [38] 控制。若位点 $(n,m)$ 上组元 $(i,j)$ 的拟议交换降低残差

$$
R = \sum_{r,(i,j)\in\Omega}(\alpha_{ij}^{(r)} - \alpha_{ij}^{\star\,(r)})^2,
$$

则接受该交换；否则以概率 $\exp(-\Delta R / T_{\rm MC})$ 接受，其中 $T_{\rm MC} = 10^{-3}$ 作为允许偶发上坡移动的虚拟温度。接受交换后，Warren-Cowley 矩阵以增量方式更新：

$$
\Delta\alpha_{ab}^{(r)} = -\frac{1}{c_b N z_r}
  \bigl(\Delta n_{ab}^{(r)}\bigr),
$$

其中 $\Delta n_{ab}^{(r)}$ 只计数位点 $n$ 和 $m$ 的第 $r$ 壳层 $z_r$ 个近邻中因组元变化而改变的键。该增量更新的每次接受交换成本为 $O(z_r K^2)$，并且在大 $K$ 和大 $N$ 时是主导成本。`anisro.benchmarks.armc` 中的 ARMC 实现使用与可微计数器相同的邻接矩阵和组元索引，以确保两种方法之间的 $\alpha$ 定义在数值上完全相同。

#### 2.9 有效对相互作用提取

2NN-MEAM 形式 [24] 将总能量定义为嵌入能和由角函数屏蔽的对势之和；它是多体势，并不直接给出 $\{V_{ij}^{(r)}\}$。我们通过把 MEAM 能量曲面投影到 NIMM 模型的对簇子空间来提取有效对相互作用：提取出的 $V_{ij}^{(r)}$ 是在目标温度下采样的一组构型中再现 MEAM Warren-Cowley 统计量的最佳拟合对能。

我们提供 3 条从任何实现 `EnergyCalculator` 协议的原子间势提取 $\{V_{ij}^{(r)}\}$ 的路线。

三能量组合。对于二元合金，1NN EPI 由 3 个体相能量得到：

$$
V_{AB}^{(1)} = U_{AA}^{\rm (bulk)} + U_{BB}^{\rm (bulk)} - 2 U_{AB}^{\rm (bulk)},
$$

其中 $U_{AA}^{\rm (bulk)}$ 和 $U_{BB}^{\rm (bulk)}$ 是相同晶格上纯 A 和纯 B 的逐原子内聚能，$U_{AB}^{\rm (bulk)}$ 是等摩尔有序结构的逐原子内聚能。这是合金形成能的晶格类比，并且在仅含对相互作用的假设下是精确的。对于 2NN 壳层，相同公式应用于第二近邻的纯元素和有序能量。

随机构型回归。对于 $K \geq 3$ 组元，三能量路线每个壳层最多为 $K(K-1)/2$ 个未知数提供 $K(K-1)/2$ 个方程，但对于具有多体特征的势，仅含对相互作用的假设会引入系统误差。因此我们最小化

$$
\mathcal{L}_{\rm EPI} = \frac{1}{N_{\rm conf}}\sum_{c=1}^{N_{\rm conf}}
  \sum_{r,(i,j)}\!\bigl(\alpha_{ij}^{(r),\,\rm NIMM}(\{V_{ij}^{(r)}\})
  - \alpha_{ij}^{(r),\,\rm MC,c}\bigr)^2,
$$

其中 $N_{\rm conf} = 60$ 个随机构型，并通过带 PyTorch autograd 的 L-BFGS 进行优化。由于 NIMM 对 $\{V_{ij}^{(r)}\}$ 可微，这是标准的基于梯度的回归。决定系数 $R^2$ 衡量 MC $\alpha$ 的方差有多少由对模型解释，其中 $R^2 \geq 0.95$ 表示仅含对相互作用的截断是足够的。

通过 `icet` 的簇展开。对于具有显著多体贡献的体系，`icet` 簇展开库 [2,33,39] 提取超过对层级的有效簇相互作用。来自 `icet` 的对 ECI 可直接输入 NIMM 前向求解器；`icet` 重构 $\alpha$ 与直接 MC $\alpha$ 在仅含对相互作用截断下的残差，用于量化多体误差。Cu-Ni 上 3 种方法的定量比较见补充信息 S2 节。

#### 2.10 晶格构建和 LAMMPS 弹性常数

FCC 超胞通过复制常规 4 原子晶胞构建，晶格常数 $a_0$ 取自 0 K 的 MEAM 势。BCC 超胞使用 2 原子体心晶胞，$a_0$ 来自相同 MEAM。壳层邻接矩阵 $A^{(r)}$ 由 $N\times N$ 距离矩阵在最小镜像周期边界条件下计算，并使用 2 个壳层截断 $r_1 < r_2$：对于 FCC，$r_1 = a_0/\sqrt{2}$ 且 $r_2 = a_0$（分别为 12 和 6 个近邻）；对于 BCC，$r_1 = a_0\sqrt{3}/2$ 且 $r_2 = a_0$（分别为 8 和 6 个近邻）。

弹性常数通过恒体积下的 Voigt 有限差分方法计算。施加 6 个应变张量 $\varepsilon$（单轴 $\varepsilon_{11}$、$\varepsilon_{22}$、$\varepsilon_{33}$ 和剪切 $\varepsilon_{12}$、$\varepsilon_{13}$、$\varepsilon_{23}$），应变幅值为 $\{\pm 0.5\%, \pm 1\%\}$；每个受应变构型在恒定胞形下通过 FIRE 最小化 [6] 松弛到 $10^{-4}$ eV/Å 的力容差，然后通过 LAMMPS `compute stress/atom` 命令评估应力张量。弹性刚度系数由四点有限差分公式提取。所有弹性常数计算都使用 108 原子 $3\times3\times3$ 超胞；这一胞尺寸选择的影响在补充信息中讨论。完整计算细节、收敛数据和所用原子间势列表见补充信息 S4-S5 节。

#### 2.11 与 Rao 和 Curtin 方程的对应关系

为保证可复现性，我们列出 Rao 和 Curtin [31] 的方程如何映射到我们的推广求解器。他们的式（8）给出簇占据对数概率；其驻定条件（他们的式 10-11）在消去 Stirling 的 $-1$ 因子并显式写出 $\ln x_{ij}^{(r)}$ 的符号后，恢复我们的驻定方程。他们的式（12）定义 $P_{ij}^{(r)}$，对应我们的联合对概率方程。他们关于 $\alpha_{ij}^{(r)}$ 的式（13）对应我们的 Warren-Cowley 参数方程。他们的式（22）中的二元 NIMM 自由能在我们的方程中推广到 $K$ 组元；只依赖成分的同质对能量项（$c_i U_{ii}$）在固定成分下为常数，因此被略去。完整推导见补充信息 S1 节。

---

### 结论

我们引入了 ANISRO，这是一个用于多主元合金短程有序逆向设计的端到端可微流程。该框架从 Rao 和 Curtin [32] 的 Non-Interacting Molecule Method 出发，将他们的二元推导推广到 $K$ 组元，并使用所得解析前向求解器来预测平衡 Warren-Cowley 参数，同时通过把设计锚定到所选原子间势的自由能曲面上来正则化逆问题。在逆向一侧，可微 Warren-Cowley 计数器通过 softmax logit 场参数化每个晶格位点，并用连续梯度下降取代随机 ARMC，在 4000 原子时实现 $6\times$ 加速和 $8\times$ 精度增益，同时透明地扩展到任意组元数。这两个组成部分连接到一个描述符 MLP 替代模型，使梯度可以从目标弹性常数一路流入逐位点 logit 场，并在单次反向传播中完成设计循环，而不需要任何有限差分 Jacobian 或伴随求解。经过 9 个 FCC 和 BCC 体系调查验证，该流程揭示了 108 原子调查小胞中 Cr-Fe-Ni 的 SRO 诱导 $C_{11}$ 变化为 $+57\,\%$，Cr-Cu-Ni 为 $-20\,\%$；跨 $3\times3\times3$ 到 $6\times6\times6$ 超胞（108-864 原子）的胞尺寸验证显示，$\Delta C_{11}$ 的符号和大小对胞尺寸敏感，整个系列中的数值从 $-16\,\%$ 到 $+24\,\%$ 不等，因此这些标志性数值应解释为单胞指标，而不是收敛的热力学平均。该流程在独立 LAMMPS-MEAM 验证中，使 4 个 Co-Cr-Ni 性能目标中的 3 个位于 6 % 以内。

---

## 结果/讨论章节子标题翻译

- 3 结果
    - 3.1 相对于 Monte Carlo 的前向 NIMM 验证
    - 3.2 ARMC 与梯度 SRO 到结构反演的比较
    - 3.3 来自原子间势的有效对相互作用
    - 3.4 多体系 FCC 和 BCC 合金调查
    - 3.5 真实 MEAM 和 MACE-MP-0 上的 Cantor 合金
    - 3.6 随体系尺寸和组元数的缩放
    - 3.7 Co-Cr-Ni 上的闭环性能设计
- 4 讨论
    - 4.1 梯度方法在哪些情况下胜出
    - 4.2 真实数据 SRO-性能目录
    - 4.3 真实数据闭环：限制与展望
    - 4.4 能量后端的选择
    - 4.5 解析 NIMM 正则化项的有效性

---

## 图题和表题翻译

图 1：ANISRO 概览。ANISRO 将任意原子间势连接到基于梯度的原子短程有序和目标力学性能设计。阶段 1（蓝色）：EPI 提取和前向 NIMM 对平衡 $\alpha$ 的预测。阶段 2（绿色）：通过软位点占据进行可微 SRO 到结构反演。阶段 3（紫色 / 橙色）：描述符替代模型和闭环性能设计，其中梯度端到端流动。小柱状图显示了 9 个被调查合金体系中 SRO 诱导的 $\Delta C_{11}$ 范围。

图 2：可微 SRO 到结构反演的概念。每个晶格位点携带一个 logit 向量 $\boldsymbol{\ell}_i \in \mathbb{R}^K$；通过逐位点 softmax 后得到软占据概率 $P_i = \sigma(\boldsymbol{\ell}_i)$。可微 $\alpha$ 计数器从 $P$ 评估 Warren-Cowley 参数，从而能够对 SRO 损失进行梯度下降。硬 top-$k$ 投影把软最优解转换为离散 LAMMPS 构型。

图 3：性能描述符和替代模型工作流。顶部（蓝色 / 绿色 / 橙色）：推断路径 $\boldsymbol{\ell}\!\to\!P\!\to\!\boldsymbol{d}\!\to\!\phi_\theta\!\to\!\hat{y}$。底部（虚线）：从 LAMMPS 标签到 MLP 权重更新的训练路径。红色路径（节点上方）：第 2.7 节闭环设计使用的端到端 autograd 梯度。

图 4：完整 ANISRO 流程。蓝色：前向 NIMM 提取有效对相互作用 $\{V_{ij}^{(r)}\}$，并通过 Newton 迭代预测 $\alpha_{\rm eq}$。绿色：可微 SRO 到结构反演，包含 logit 场 $\boldsymbol{\ell}$、软占据 $P=\sigma(\boldsymbol{\ell})$、可微 $\alpha$ 计数器，以及由 Adam 最小化的四项损失。紫色：描述符 MLP $\phi_\theta$ 在 $[c,\alpha^{(1)},\alpha^{(2)},\sigma_{\rm occ}]$ 上训练。橙色：闭合设计循环通过 $\phi_\theta$ 和可微计数器把性能误差反向传播到 logit 场中。

图 5：相对于 Cu-Ni Metropolis Monte Carlo 的前向 NIMM 验证。3 种成分（$c_{\rm Cu} = 0.5, 0.3, 0.1$）、$T = 300\,\mathrm{K}$、$5\times5\times5$ FCC 超胞下，Warren-Cowley $\alpha_1$ 随约化对逸度 $x_{12}^{(1)}$ 的变化。阴影带：对簇有效窗口 $0.5 < x < 1.5$ [31]。在该窗口内，NIMM 和 MC 的一致性达到 $|\Delta\alpha| < 0.03$。

图 6：Cu$_{50}$Ni$_{50}$（$4\times4\times4$，256 原子）上 ARMC、梯度和混合方法的损失随壁钟时间变化，包含 5 个目标 $\alpha$ 元组和 5 个随机种子，时间预算为 8 s。在该胞尺寸下，ARMC 达到约 $50\times$ 更低的残差；两种方法都保持在 $|\Delta\alpha| < 0.02$ 内。

图 7：Co-Cr-Ni（$4\times4\times4$ FCC，256 原子）原子结构，由梯度逆设计（左）和 ARMC（右）生成，二者均以 $\alpha_{\rm CoCr}^{(1)} = -0.38$ 为目标。[001] 俯视 slab，2 个原子层；原子按组元着色（Co = 橙色，Cr = 蓝色，Ni = 绿色）。两种方法都编码了相同的 Co-Cr 异质对富集。结构作为 LAMMPS 数据文件导出，并直接从原子坐标渲染。

图 8：Cu-Ni MEAM 上的 EPI 提取交叉验证。3 条路线（三能量、60 个构型上的回归、`icet` 对簇展开）被输入前向 NIMM 求解器，并在 $T \in \{300, 500, 1000\}\,\mathrm{K}$ 下与 Metropolis MC $\alpha$ 比较。所有路线都给出 $V_1 > 0$（有序化），并在 0.01-0.03 内再现 MC $\alpha$。

表 1：真实 MEAM SRO-性能调查。对于每个体系，该表报告 EPI 回归质量 $R^2$、300 K 下来自 Metropolis MC 的主导 Warren-Cowley 参数，以及在 108 原子 $3\times3\times3$ 超胞上由 LAMMPS-MEAM 测得的、梯度设计构型和相同成分随机参照构型之间的 SRO 诱导内聚能和弹性模量变化。正的 $\Delta C_{11}$ 表示硬化；负值表示软化。

图 9：表 1 中的 SRO 诱导性能变化。柱：梯度设计构型与随机参照构型之间的 $\Delta C_{11}$（左轴）、$\Delta C_{44}$（中轴）和 $\Delta E_{\rm coh}$（右轴），由 LAMMPS-MEAM 在 108 原子 $3\times3\times3$ 超胞上计算。Cr-Fe-Ni 显示最大的 $C_{11}$ 硬化（$+57\,\%$）；Cr-Cu-Ni 显示最大的软化（$-20\,\%$）。

图 10：梯度设计的 Cr-Fe-Ni 构型原子结构（$4\times4\times4$ FCC，256 原子），[001] 俯视图，2 层 slab。Cr（蓝色）、Fe（红色）和 Ni（绿色）原子。Cr-Fe 异质对富集（$\alpha_{\rm CrFe}^{(1)} = -0.31$）直接可见，形成了导致 $+57\,\%$ $\Delta C_{11}$ 信号的刚性 Cr-Fe 键网络。

图 11：使用 Choi-Lee 2NN-MEAM [11] 的 Cantor 合金（CoNiCrFeMn）。左：300 K 下所有 10 个异质对的 NIMM 预测与 MC $\alpha$ parity。右：256 原子胞上 ARMC 与梯度逆设计的壁钟时间损失。梯度方法在 5.5 s 内使所有对达到 $|\Delta\alpha|<0.07$；ARMC 在 5 组元时需要约 60 s。

图 12：梯度设计的 Cantor 合金结构（CoNiCrFeMn，$4\times4\times4$ FCC，256 原子，2 层 slab）的等轴视图。5 个组元为 Co（橙色）、Ni（绿色）、Cr（蓝色）、Fe（红色）和 Mn（紫色）。主导 Ni-Mn 回避有序（$\alpha_{\rm NiMn}\approx+0.96$）表现为 Ni（绿色）和 Mn（紫色）原子之间的空间分离。

图 13：通过 `AseCalculator` 使用 MACE-MP-0 的相同 Cantor 合金流程。主导 motif 从 Ni-Mn 回避（MEAM，图 11）转变为 Co-Fe 有序，揭示了两种势之间的定性化学差异，同时不改变任何面向用户的代码。

图 14：Co-Cr-Ni（Choi-Lee 2NN-MEAM [11]）在 256、864 和 4000 原子下的缩放。目标：300 K 下 Metropolis MC 平衡 $\alpha$。在 4000 原子时，ARMC 在 7 min 内未能收敛（最大误差 0.439），而梯度方法在 71 s 内达到最大误差 0.054，快 $6\times$ 且精度高 $8\times$。

图 15：Co-Cr-Ni（Choi-Lee 2NN-MEAM [11]）上的闭环性能设计。左：按目标 $\alpha$ 着色的 50 个设计构型。右：4 个目标 $C_{11}$ 值（虚线）与 LAMMPS 实际值（圆点）和替代模型预测值（叉号）。4 个中有 3 个落在 6 % 以内；240 GPa 离群点落在替代模型的外推区间。

表 2：Co-Cr-Ni（Choi-Lee 2NN-MEAM [11]）上的闭环 $C_{11}$ 验证。对于每个目标，梯度通过替代模型和可微 $\alpha$ 计数器流入 logit 场（1500 个 Adam 步）；然后通过独立 LAMMPS 弹性常数计算验证硬投影结构。

图 16：总览总结。（A）固定壁钟时间下 Cu$_{50}$Ni$_{50}$ 上的 ARMC、梯度和混合方法：ARMC 在 256 原子时胜出，梯度在超过 864 原子后胜出。（B）跨体系 SRO 诱导的 $\Delta C_{11}$：Cr-Fe-Ni $+57\,\%$ 硬化（最大），Cr-Cu-Ni $-20\,\%$ 软化。（C）缩放包络：在 4000 原子时，梯度比 ARMC 快 $6\times$ 且精度高 $8\times$。（D）Co-Cr-Ni 上的闭环 $C_{11}$ 验证：4 个目标中有 3 个位于 6 % 以内。

表 3：Co-Cr-Ni 弹性常数：与已发表数值的比较。$\Delta C_{11}$ 是相对于随机合金参照的 SRO 诱导变化。破折号表示被引用工作中未报告的数值。

