# 文献总结 - 用于溶液中从头算自由能计算的炼金热力学积分 - 2026

## 文献基本信息

- 英文原文标题：Alchemical thermodynamic integration for ab initio free-energy calculations in solutions
- DOI 链接：论文原文未给出 DOI；外部检索未确认正式 DOI。
- 作者：Liangrui Wei，Feng Zhang，Renata M. Wentzcovitch，Kai-Ming Ho，Yang Sun
- 作者单位：Department of Physics, Xiamen University, China；Department of Physics and Astronomy, Iowa State University, United States；Ames National Laboratory, United States；Department of Applied Physics and Applied Mathematics, Columbia University, United States；Department of Earth and Environmental Sciences, Columbia University, United States；Lamont-Doherty Earth Observatory, Columbia University, United States
- 期刊名称：论文原文未给出。
- 投稿 - 返修 - 接收 - 在线发表日期：论文原文未给出投稿、返修、接收和在线发表日期；首页仅标注 Dated: July 20, 2026。
- 数据/代码链接：论文原文未列出数据或代码开源链接。正文提到实现中使用 `input.json`、`vasp_plugin.py` 和 `MCMD.py`，但未给出仓库地址。

## 文献总结

### 研究背景与科学问题

本文面向溶液体系的第一性原理自由能计算。Gibbs 自由能决定有限温度下不同相的热力学稳定性和相图，而它同时包含焓与熵两部分。AIMD 可以直接采样焓相关贡献，但熵不是标准 MD 或 MC 模拟中的直接观测量。因此，以从头算精度可靠获得自由能仍是计算物理和计算材料科学中的核心困难。

已有策略之一是引入显式熵模型，例如从短程有序或关联函数近似超额熵。这类方法计算成本较低，也容易与 AIMD 焓计算结合，但预测能力依赖熵模型本身和假设的超额项。另一类更严格的方法是 Hamiltonian thermodynamic integration（HTI），即通过把参考 Hamiltonian 转换为目标 Hamiltonian 来计算自由能差。传统 HTI 常以 Lennard-Jones 或 Uhlenbeck-Ford 等具有已知自由能的解析参考体系为起点，也可引入经典势作为中间 Hamiltonian，以避免参考态和目标态差异过大时积分路径不良或穿越相变。

对于相图构建而言，很多情况下并不需要绝对自由能，只需要相对于合适端元的 Gibbs 自由能差即可确定混合自由能。作者据此强调，“炼金”路径特别适合溶液自由能计算：沿该路径将纯液体逐渐变为液体溶液，纯端元与目标溶液物理相似，因此积分路径更平滑。此前这种思路已在具有显式相互作用形式的经典势中实现；但扩展到从头算框架并不直接，因为 DFT Hamiltonian 不能像经典势那样直接在 MD 代码中解析操控。实际实现需要在同一原子构型上同时计算两个 DFT 体系的能量和力，并在 AIMD 过程中在线耦合。

本文的科学问题就是构建一种实用的从头算 alchemical thermodynamic integration（ATI）方案，使溶液体系可以在不依赖显式熵假设、不拟合中间经典势的前提下，直接计算相对于端元的自由能差。

### 方法思想与实现框架

作者提出的 ATI 方法以溶液 $A_{1-x}B_x$ 为目标体系，并以纯 $A$ 为参考端元。为处理质量差异，先引入辅助体系 $A_{1-x}B'_x$，其中 $B'$ 与 $B$ 质量相同，但与其他原子的相互作用按照 $A$ 处理。这样，自由能差被拆分为质量项 $F_{mass}$、热力学积分项 $F_{TI}$ 和体积/状态方程项 $F_{PV}$。

核心热力学积分通过 λ 依赖 Hamiltonian 完成：

$$
H_\lambda = (1-\lambda)H_{A_{1-x}B'_x}+\lambda H_{A_{1-x}B_x}.
$$

在从头算模拟中，$H_{A_{1-x}B'_x}$ 和 $H_{A_{1-x}B_x}$ 没有可直接传给 MD 引擎的显式解析形式，因此作者改为耦合两个 DFT 计算返回的力：

$$
f_\lambda = (1-\lambda)f_{A_{1-x}B'_x}+\lambda f_{A_{1-x}B_x}.
$$

这正是本文实现的中心特征：两个常驻 DFT 计算器在同一原子构型上并行计算能量和力，再把耦合后的力和能量传给外部 MC/MD runner。当前实现中，VASP 作为 DFT 计算器，LAMMPS 负责更新原子位置，`vasp_plugin.py` 在 DFT 计算器和 MC/MD runner 之间传递结构、力和能量，`MCMD.py` 控制 MD 推进、λ 耦合和可选 MC 采样。两个 VASP 进程沿同一离子轨迹持续运行，因此波函数和电荷密度可以从内存中保存的已收敛状态外推，避免反复重启 DFT 计算带来的额外开销。

### 计算设置

DFT 计算使用 VASP。电子-离子相互作用采用 PAW 方法，交换关联泛函采用 GGA-PBE。高温电子熵用 Mermin 泛函描述，电子温度设为与离子温度一致。

Fe-Ni 模拟中，Fe 和 Ni 使用 PAW-PBE 势，价电子分别为 Fe 的 $3d^64s^2$ 和 Ni 的 $3d^84s^2$。平面波截断能为 400 eV，液体超胞含 250 个原子，AIMD 和 ATI 时间步长为 1.0 fs。Nosé-Hoover 热浴阻尼时间为 $\tau=0.01$ ps。

Li-Na 模拟中，Li 和 Na 使用 PAW 势，价电子分别为 Li 的 $2s^1$ 和 Na 的 $3s^1$。平面波截断能为 200 eV，超胞含 500 个原子，Brillouin 区在 AIMD 和 ATI 中均用 Γ 点采样，AIMD 和 ATI 时间步长为 2.0 fs。Nosé-Hoover 热浴阻尼时间为 $\tau=0.02$ ps。

对于 MCMD 耦合，作者使用 LAMMPS 的 `fix atom/swap` 功能，并遵循已有 atom-swap 方案。在 $Li_{0.6}Na_{0.4}$ 情形中，每 10 个 MD 步尝试一次原子交换，并按照 Metropolis 概率 $P=\min[1,\exp(-\Delta E/k_BT)]$ 接受，其中 $\Delta E$ 是试探交换导致的总能变化。

### 经典 Fe-Ni 液体基准

作者首先用经典 Fe-Ni 液体检验 ATI 工作流中最关键的“两个 Hamiltonian 力和能量耦合”是否正确。该基准以 LAMMPS 中已有的 `pair/hybrid` 功能作为可直接对照的混合势实现。两个炼金端态由 Fe-Ni EAM 势和两种 `pair_coeff` type mapping 生成：参考态为 Fe Fe，目标态为 Fe Ni。

比较结果表明，ATI 代码得到的两个耦合 Hamiltonian 势能演化曲线能够复现 LAMMPS 原生 `pair/hybrid` 结果，说明 ATI driver 正确耦合了两个计算器返回的力和能量，并能按预期更新原子位置。

作者还用 Fe-Ni EAM 基准估计 TI 自由能差中的有限尺寸与采样误差。对于 AIMD 可达到的体系尺寸和模拟长度，即约 200 个原子、约 10 ps 量级，计算结果相对于 10000 个原子、200 ps 长采样极限的偏差小于 2 meV/atom。这一结果为后续从头算 ATI 中有限采样误差的量级提供了参考。

### 从头算 Fe-Ni 液体自由能验证

作者随后计算 Fe90Ni10 在 6000 K 和 323 GPa 下的从头算混合自由能，并与此前基于 regular-solution（RS）模型的从头算结果比较。该测试中，λ 依赖力来自两个使用不同 PAW 势设置的 DFT 计算，A 对应 Fe，B 对应 Ni。炼金路径以纯 Fe 为参考端元，沿路径将 Fe 替换为 Ni'。

ATI 计算使用 6 个 λ 点：0、0.2、0.4、0.6、0.8 和 1.0。每条轨迹包含 0.5 ps 平衡和 4.5 ps 数据采集。λ = 0.6 的能量随时间演化显示合理涨落，说明体系达到平衡，耦合方案稳定。

通过对 λ 依赖炼金 integrand 的二次多项式拟合并积分，得到 $F_{TI}=0.315 \pm 0.001$ eV/atom。由 P-V 关系计算的 $F_{PV}$ 仅为 0.00004 eV/atom，原因是 Fe 和 Ni 在该高压高温条件下原子体积非常接近。质量项 $F_{mass}$ 为 -0.172 eV/atom。因此，Fe90Ni10 相对于纯 Fe 的 Gibbs 自由能差为 $0.143 \pm 0.001$ eV/atom。该值与参考文献 [18] 中相同体系尺寸 AIMD 和 RS 模型得到的 0.143 eV/atom 一致。

这一结果验证了本文 ATI 方案的准确性，也说明在该条件下液态 Fe90Ni10 可以被 RS 模型良好描述。

### 从头算 Li-Na 液体溶液应用

Li-Na 液体溶液是本文的主要应用体系之一。实验 Li-Na 相图存在显著低温 miscibility gap，已有从头算研究也可作为对照。作者在 473 K、常压附近计算 $Li_xNa_{1-x}$ 的自由能，并比较此前 AIMD 结合熵模型的结果以及实验相分离边界。

与 Fe-Ni 不同，Li 和 Na 原子体积差异很大，因此 $F_{PV}$ 项变得重要。作者首先对 $x_{Li}=0.2,0.4,0.6,0.8,1.0$ 的液体体系在 5 个不同体积下开展 AIMD，获得接近 0 GPa 的 P-V 关系，并用 Birch-Murnaghan 状态方程拟合得到各成分在 0 GPa 和 473 K 下的平衡体积。计算体积与 Huang 等人的 AIMD 结果一致，但比实验值系统性低约 2%，作者将其归因于 DFT 交换关联泛函低估平衡体积的已知效应。

随后，作者对纯 Na 的 P(V) 曲线进行更宽体积范围的 AIMD 计算，并用三阶 Birch-Murnaghan 状态方程拟合。该 P(V) 曲线用于计算 $F_{PV}$。

ATI 模拟覆盖 $x_{Li}=0.1,0.15,0.2,0.4,0.6,0.8,0.85,0.9,0.95,1.0$，λ 点为 0、0.25、0.5、0.75 和 1.0。纯 Na 作为参考端元，沿炼金路径将 Na 逐渐替换为 Li。每条轨迹包含 1 ps 平衡和 10 ps ATI 采样。所有成分的 integrand 都随 λ 平滑变化，说明热力学积分收敛良好。

对于倾向相分离的 $Li_{0.6}Na_{0.4}$，作者使用 MCMD runner 测试收敛性。两个独立的 10 ps MCMD 运行给出几乎相同的能量。λ 从 0 到 0.75 时，MD 和 MCMD 结果几乎不可区分；在 λ = 1.0 即真实 $Li_{0.6}Na_{0.4}$ 体系中，MCMD 能量比 MD 低 0.004 eV/atom。作者将其归因于 MCMD 能更接近平衡，特别是在体系有相分离倾向时。配对关联函数显示，从 Li'Na 到真实 Li-Na 体系只发生小变化，且体系在模拟中保持空间均匀单相，因此作者获得的是均匀混合相的自由能。

自由能分解显示，$F_{TI}$ 随 Li 含量增加而变得更负，$F_{PV}$ 为正并抵消相当一部分下降，因此 Li-Na 中 EOS 相关贡献远大于 Fe-Ni。混合 Gibbs 自由能可由 $G_{mix}(x)=\Delta G(x)-x\Delta G(1)$ 得到。ATI 结果在富 Li 与贫 Li 端都接近 Huang 等人 473 K 的自由能数据，偏差约 1 meV/atom。$x_{Li}=0.6$ 时，MCMD-ATI 自由能比 MD-ATI 低约 0.5 meV/atom。

作者用 Redlich-Kister 表达式拟合自由能曲线。大部分自由能曲线在 $x_{Li}=0.1-0.95$ 组成范围内高于凸包，表明相对于液-液相分离热力学不稳定。所得相分离区间与实验观察到的 $x_{Li}=0.15$ 到 0.95 的相分离范围一致。富 Li 侧吻合很好，富 Na 侧边界偏差略大；作者认为该偏差可由 DFT 约 1 meV/atom 精度限制和图 2(b) 所示约 2 meV/atom 有限尺寸误差解释，因为这种能量不确定度足以移动计算相边界。

### 计算效率

作者比较 AIMD、ATI 和经典势测试中的每 MD 步 wall time。由于 ATI 并行运行两个 DFT 计算器，其 CPU 使用量约为标准 AIMD 的两倍；但 wall time 更能反映实际 time-to-solution。

当前实现的主要额外开销来自 `vasp_plugin.py` 接口传递能量、力和原子构型，涉及 force calculator 与 MD runner 之间的 callback 和数据交换。对于从头算模拟，电子结构计算本身耗时远大于这一接口开销，因此 ATI 的 wall time 在所测试体系尺寸中接近标准 AIMD。对于经典势，由于力计算非常便宜，接口开销明显，ATI-经典 MD 比 LAMMPS 原生 `pair/hybrid` 慢约一个数量级。作者指出，ATI 的目标本来就是不能直接在经典 MD 引擎中耦合的从头算 Hamiltonian，因此接近 AIMD 的 wall-time 性能对于第一性原理应用是令人满意的。

### 主要贡献与局限

本文的主要贡献是提出并实现了一个面向溶液体系的从头算 ATI 工作流。该工作流将两个常驻力和能量计算器与外部 MC/MD runner 耦合，使两个炼金端态的力和能量能够在 MC/MD 模拟过程中在线组合。它绕过了显式熵模型和中间经典势拟合需求，也不要求目标 Hamiltonian 具有可解析操控形式。

经典 Fe-Ni 基准验证了力和能量耦合实现的正确性；从头算 Fe-Ni 高压高温液体验证了该方案能再现已有 RS 模型结果；Li-Na 液体应用显示，ATI 能处理原子体积差异显著、$F_{PV}$ 重要、并具有液-液相分离倾向的溶液体系。性能测试进一步说明，在从头算场景中，ATI 的 wall time 接近标准 AIMD。

论文中也可见若干边界条件：当前实现以 VASP 和 LAMMPS 为具体后端；论文未给出公开代码仓库；Li-Na 相边界仍受 DFT 精度和有限尺寸误差影响；对于强相分离体系，必须注意通过 MD/MCMD 采样获得均匀混合相自由能，而不是让体系在模拟中直接发生空间相分离。

## 摘要翻译

我们开发了一种炼金热力学积分方案，该方案在 Monte Carlo 和分子动力学模拟过程中即时耦合从头算力计算器。该实现通过与已有 hybrid-Hamiltonian 方法对比进行了验证。该方案给出了高压 Fe-Ni 和常压 Li-Na 液体溶液的从头算自由能，这些自由能与此前计算一致，并再现实验观察到的 Li-Na miscibility gap。该代码具有与标准从头算分子动力学相当的效率。这些结果确立了该方案作为一种实用的炼金积分框架，可用于溶液中的第一性原理自由能计算。

## 引言翻译

Gibbs 自由能在计算材料科学中居于中心地位，因为它定义了在一系列热力学条件下竞争相的稳定性和相图 [1]。在有限温度下，Gibbs 自由能由焓和熵共同决定。虽然从头算分子动力学（AIMD）可以常规采样焓贡献，但熵并不是标准分子动力学（MD）或 Monte Carlo（MC）模拟中的直接可观测量。因此，以从头算精度可靠地获得自由能，仍然是计算物理中的主要挑战之一。

一种常见策略是使用显式熵模型评价自由能，其中熵项以解析方式定义，而超额熵则由结构信息近似，例如短程有序 [2] 或关联函数 [3]。虽然这种方法计算成本相对较低，并且容易与 AIMD 中的焓计算结合，但其预测能力最终取决于熵模型和所假定超额项的有效性。更严格的方法是使用 Hamiltonian thermodynamic integration（HTI），该方法通过将参考 Hamiltonian 转换为目标 Hamiltonian 来计算自由能差。在这一框架中，人们通常引入具有已知自由能的参考体系，例如解析 Lennard-Jones 和 Uhlenbeck-Ford 体系 [4,5]。然而，如果参考体系和目标体系差异很大，积分路径可能变得行为不良，甚至穿过相变。一种补救方法是使用精心设计的经典势作为中间 Hamiltonian，将解析模型与从头算目标结合起来 [6-9]。

对于相图构建而言，绝对自由能通常并非必要。相反，相对于合适端元的相对 Gibbs 自由能足以确定混合自由能。因此，一条把纯液体转变为液体溶液的“炼金”路径特别适合溶液的自由能计算，因为纯端元提供了物理上相似的参考态，从而提供平滑的积分路径 [10]。这种基于 HTI 的策略已经使用具有显式原子间相互作用形式的经典势得到展示 [10]。然而，将这一思想扩展到从头算框架并非平凡。与可以直接操控 Hamiltonian 的经典 MD 模拟不同，从头算实现要求对具有相同原子构型的两个体系用密度泛函理论（DFT）评价能量和力，并随后在 AIMD 中即时一致地耦合它们。因此，需要一种实用且常规的从头算 alchemical thermodynamic integration（ATI）方案来进行自由能计算。

在本文中，我们开发了一种用于溶液体系的 ATI 代码。通过将两个 DFT 力和能量计算器耦合到一个外部 MD runner，该方法能够沿炼金路径高效采样，并直接评价相对自由能，而不依赖显式熵假设或拟合中间经典势。我们使用经典和从头算 Fe-Ni 基准，以及一个从头算 Li-Na 液体溶液应用来展示该代码。

本文组织如下。第 2 节描述 ATI 理论、实现和模拟细节。第 3 节给出验证和应用示例，包括 Fe-Ni 和 Li-Na 液体溶液基准。第 4 节报告计算性能。第 5 节总结结论。

## 方法翻译

### 2. 理论与实现

### 2.1 炼金热力学积分

我们首先回顾 ATI 的算法。考虑一个溶液体系 $A_{1-x}B_x$，其中 $A$ 和 $B$ 是不同类型的原子，$x$ 是 $B$ 的浓度。通过引入辅助体系 $A_{1-x}B'_x$，可以计算 $A_{1-x}B_x$ 与纯 $A$ 之间的 Helmholtz 自由能差；在该辅助体系中，$B'$ 原子具有与 $B$ 相同的质量，但与其他原子的相互作用与 $A$ 相同。由质量差异导致的 $A_{1-x}B'_x$ 与 $A$ 之间的 Helmholtz 自由能差可写为

$$
F_{mass}=F_{A_{1-x}B'_x}-F_A=k_BT\left[x\ln\frac{m_B}{m_A}+x\ln x+(1-x)\ln(1-x)\right].
$$

随后，$A_{1-x}B_x$ 与 $A_{1-x}B'_x$ 之间的自由能差可通过 HTI 得到：

$$
F_{TI}(V_0)=F_{A_{1-x}B_x}-F_{A_{1-x}B'_x}
=\int_0^1\left\langle\frac{\partial H_\lambda}{\partial\lambda}\right\rangle_{\lambda,V_0,T}d\lambda
=\int_0^1\left\langle U_{A_{1-x}B_x}-U_{A_{1-x}B'_x}\right\rangle_{\lambda,V_0,T}d\lambda,
$$

其中 $\langle\cdots\rangle_{\lambda,V_0,T}$ 表示在 $V_0$ 下使用耦合 Hamiltonian

$$
H_\lambda=(1-\lambda)H_{A_{1-x}B'_x}+\lambda H_{A_{1-x}B_x}
$$

进行的 MD 模拟。在 AIMD 中，Hamiltonian $H_{A_{1-x}B'_x}$ 和 $H_{A_{1-x}B_x}$ 没有显式解析或数值形式。因此，原子位置只能使用耦合力更新：

$$
f_\lambda=(1-\lambda)f_{A_{1-x}B'_x}+\lambda f_{A_{1-x}B_x}.
$$

因此，ATI 代码在同一原子构型上使用两个并行 DFT 计算评价力和能量，这是当前实现的中心特征。结合式 (1) 和式 (2)，在相同体积 $V_{A_{1-x}B_x}$ 下，$A_{1-x}B_x$ 与纯 $A$ 之间的 Helmholtz 自由能差为

$$
F_{A_{1-x}B_x}(V_{A_{1-x}B_x})-F_A(V_{A_{1-x}B_x})
=F_{mass}+F_{TI}(V_{A_{1-x}B_x}).
$$

利用 Helmholtz 自由能差，可以计算 Gibbs 自由能差。我们用 $V_{A_{1-x}B_x}$ 和 $V_A$ 表示在给定压力 $P_0$ 下 $A_{1-x}B_x$ 和 $A$ 的体积。根据 $G=F+PV$ 和 $P=-(\partial F/\partial V)_T$，得到

$$
\begin{aligned}
G_{A_{1-x}B_x}(P_0)-G_A(P_0)
=&F_{A_{1-x}B_x}(V_{A_{1-x}B_x})-F_A(V_{A_{1-x}B_x})\\
&+P_0V_{A_{1-x}B_x}-P_0V_A-\int_{V_A}^{V_{A_{1-x}B_x}}P_A(V)dV,
\end{aligned}
$$

其中 $P_A(V)$ 是纯 $A$ 的状态方程（EOS）。结合上述关系，我们得到

$$
G_{A_{1-x}B_x}(P_0)-G_A(P_0)
=F_{TI}(V_{A_{1-x}B_x})+F_{mass}+F_{PV}.
$$

$F_{PV}$ 项表示由 $A_{1-x}B_x$ 与 $A$ 之间 EOS 差异造成的自由能贡献：

$$
F_{PV}=P_0V_{A_{1-x}B_x}-P_0V_A-\int_{V_A}^{V_{A_{1-x}B_x}}P_A(V)dV.
$$

### 2.2 模拟细节

DFT 计算使用 Vienna ab initio simulation package（VASP）[11] 完成。采用 projector-augmented-wave（PAW）方法描述电子-离子相互作用，并使用 Perdew-Burke-Ernzerhof（PBE）形式的 generalized gradient approximation（GGA）作为交换关联泛函。高温电子熵由 Mermin 泛函 [12,13] 描述。Mermin 泛函中的电子温度被设为与离子温度相同。

对于 Fe-Ni 模拟，Fe 和 Ni 使用 PAW-PBE 势，其中 Fe 的价电子为 $3d^64s^2$，Ni 的价电子为 $3d^84s^2$。平面波截断能设为 400 eV。使用包含 250 个原子的超胞模拟液体。AIMD 和 ATI 模拟的时间步长为 1.0 fs。使用 Nosé-Hoover 热浴 [14]，阻尼时间为 $\tau=0.01$ ps。

对于 Li-Na 模拟，Li 使用具有 $2s^1$ 价电子的 PAW 势，Na 使用具有 $3s^1$ 价电子的 PAW 势。平面波截断能设为 200 eV。模拟中使用包含 500 个原子的超胞。在 AIMD 和 ATI 模拟中均使用 Γ 点采样 Brillouin 区。AIMD 和 ATI 模拟的时间步长为 2.0 fs。使用 Nosé-Hoover 热浴 [14]，阻尼时间为 $\tau=0.02$ ps。

Large-scale Atomic/Molecular Massively Parallel Simulator（LAMMPS）[15] 用于在 ATI 代码中更新原子位置。对于与 Monte Carlo 采样的耦合（MCMD），我们使用 LAMMPS 的 `fix atom/swap` 功能 [15]，并遵循 [16] 中描述的 atom-swap 方案。在 $Li_{0.6}Na_{0.4}$ 情形中，每 10 个 MD 步尝试一次交换，并按照 Metropolis 概率 $P=\min[1,\exp(-\Delta E/k_BT)]$ 接受，其中 $\Delta E$ 是由尝试交换导致的总能变化。

### 2.3 代码框架

图 1 总结了 ATI 代码的工作流。计算由 `input.json` 初始化，该文件定义 ATI 模拟的输入参数。初始原子构型 $\{r_i\}$ 被提供给两个常驻 DFT 计算器，记作 DFT1 和 DFT2。两个计算器对两个 DFT 设置评价力和能量，并通过后端接口返回它们。这些力和能量被传递给 MC/MD runner，在那里使用式 (3) 构造 λ 依赖耦合力，以更新原子位置。当启用 MC 采样时，它还会按预设 MC 间隔通过交换原子生成试探构型，并使用耦合能量接受或拒绝每一次试探移动，从而更新原子构型。该循环持续到达到用户指定的 MD 步数，随后 MC/MD runner 和两个 DFT 子进程终止。

在当前实现中，VASP 作为 DFT 计算器，`vasp_plugin.py` 在 DFT 计算器和 MC/MD runner 之间传递结构、力和能量。LAMMPS 用作 MC/MD 引擎，而 `MCMD.py` 控制 MD 推进、λ 耦合和可选 MC 采样。由于两个 VASP 进程沿同一离子轨迹保持活跃，波函数和电荷密度可以从存储在内存中的先前已收敛状态高效外推 [17]。这避免了与重启 DFT 计算相关的开销，并提高了电子收敛效率。

## 结果/讨论章节子标题翻译

- 3. 结果与讨论
- 3.1 经典 Fe-Ni 液体溶液
- 3.2 从头算 Fe-Ni 液体溶液
- 3.3 从头算 Li-Na 液体溶液
- 4. 计算性能

## 结论翻译

我们已经开发了一种 ATI 代码，用于评价溶液体系中的自由能。该实现将两个常驻力和能量计算器耦合到一个外部 MC/MD runner，使来自两个炼金端态的力和能量能够在 MC/MD 模拟过程中即时组合。我们使用经典和从头算基准验证了该实现。对于经典 Fe-Ni 液体，ATI 结果再现了 LAMMPS 原生 `pair/hybrid` 实现的结果，证实该代码正确耦合了来自两个 Hamiltonian 的力和能量。对于高压高温条件下的 Fe-Ni 液体，ATI 给出的 Gibbs 自由能与此前基于 regular-solution 模型的从头算结果高度一致。我们还将该方法应用于 Li-Na 液体溶液，其中 Li 和 Na 之间的大体积差异使 EOS 相关贡献变得重要。计算得到的自由能与此前从头算数据一致，并很好地捕捉了实验观察到的液-液相分离倾向。性能测试表明，ATI 的 wall time 仍接近标准 AIMD。

由于该方法只需要计算器返回的能量和力，它不限于具有显式解析或数值形式的 Hamiltonian。这一特征使 ATI 可用于一般第一性原理和机器学习力计算器；在这些情形中，直接操控 Hamiltonian 通常是困难的。展望未来，同样基于计算器的设计可以扩展到其他 DFT 软件包和机器学习势，为使用 MC 和 MD 采样进行自由能计算提供一种通用炼金积分框架。

## 图题和表题翻译

图 1 ATI 工作流示意图。蓝色标签表示主要 Python 代码。

图 2 经典 Fe-Ni 体系的基准测试。（a）比较由 LAMMPS `pair/hybrid` 功能和当前 ATI 代码得到的 FeNi' 与 FeNi 体系势能，下方面板显示差值 $\Delta U=U_{pair/hybrid}-U_{ATI}$。（b）由 TI 得到的自由能随体系尺寸和模拟时间的变化。

图 3 Fe90Ni10 的 ATI 自由能计算细节。（a）在 6400 K 和 λ = 0.6 下，一次 ATI 模拟中来自两个 Hamiltonian 的势能随时间演化的代表性结果。（b）液态 Fe90Ni10 在 6400 K 下 integrand $\langle U_{FeNi}-U_{FeNi'}\rangle$ 随 λ 的变化。实线为二次拟合曲线。（c）Fe 和 Fe90Ni10 液体在 6400 K 下的 P-V 关系。每个压力由 5.0 ps AIMD 计算得到。（d）$F_{TI}$、$F_{mass}$ 和 $F_{PV}$ 对 Fe 和 Fe90Ni10 液体之间 Gibbs 自由能差的贡献。

图 4 473 K 下液态 $Li_xNa_{1-x}$ 的 P-V 关系。（a）不同 Li 浓度下接近 0 GPa 的 P-V 关系。每个数据点由 1 ps 平衡和随后 8 ps AIMD 模拟获得。曲线使用 Birch-Murnaghan 状态方程拟合。（b）体积随 Li 浓度的变化，并与 Jost 等人 [19] 的实验数据和 Huang 等人 [21] 的 AIMD 结果比较。红线为用于获得任意成分体积的二次拟合。（c）覆盖液态 $Li_xNa_{1-x}$ 体积范围的液态 Na 的 P-V 关系。曲线为三阶 Birch-Murnaghan EOS。

图 5 473 K 下 Li-Na 液体的自由能计算。（a）不同 Li 浓度下，炼金 integrand $\langle U_{LiNa}-U_{Li'Na}\rangle$ 随 λ 的变化。实线为二次拟合。（b）在 $x_{Li}=0.6$ 下使用 MD 和 MCMD 模拟进行的 ATI 计算。每次运行持续 10 ps。曲线为 ATI-MD 数据的二次拟合。插图显示由 MCMD（实线）和 MD（虚线）模拟得到的配对关联函数，它们在 λ 值上重叠。（c）$F_{TI}$、$F_{mass}$ 和 $F_{PV}$ 对相对于纯 Na 的 Gibbs 自由能差随 Li 浓度变化的贡献。（d）混合 Gibbs 自由能 $G_{mix}(x)$。实线为使用 Redlich-Kister（RK）模型的拟合：

$$
G_{mix}(x)=x(1-x)(2.9776+0.6524x)+473k_B[x\ln(x)+(1-x)\ln(1-x)]
$$

单位为 eV/atom。水平虚线表示 RK 模型预测的相分离边界。蓝色符号为 Huang 等人 [21] 此前计算的数据。竖直虚线表示实验测量的相分离边界 [19,20]。

图 6 ATI 实现的计算效率。不同实现中每个 MD 步的 wall time 随体系尺寸的变化。

表题：论文正文未包含表格。
