# 文献总结 - sp 能带不敏感性保护 CrMnFeCoNi 残余电阻率免受原子短程有序影响 - 2026

---

## 文献基本信息

- **英文标题**：Insensitivity of sp-bands protects the residual resistivity of CrMnFeCoNi from atomic short-range order
- **DOI**：https://doi.org/10.1016/j.scriptamat.2026.117644
- **作者**：Nicolas F. Piwek、Christopher D. Woodgate、Alberto Marmodoro、Heinz P. Huber、Ján Minár、David Redka
- **作者单位**：
    - a Department of Applied Sciences and Mechatronics, Munich University of Applied Sciences HM, Munich, Germany
    - b H.H. Wills Physics Laboratory, University of Bristol, Royal Fort, Bristol, BS8 1TL, United Kingdom
    - c Department of Physics, University of Warwick, Coventry, CV4 7AL, United Kingdom
    - d New Technologies Research Center, University of West Bohemia, Pilsen, Czech Republic
    - e FZU – Institute of Physics of the Czech Academy of Sciences, Cukrovarnická 10, CZ-162 53 Prague, Czech Republic
    - f Faculty of Nuclear Sciences and Physical Engineering, Czech Technical University in Prague, Prague, Czech Republic
- **期刊**：Scripta Materialia（Journal Pre-proof）
- **日期**：投稿 17 July 2026；返修 30 September 2026；接收 21 October 2026；在线发表 原文未提供（稿件页脚标注 22 October 2026）
- **数据与代码链接**：研究数据可向通讯作者索取；数据公开链接原文未提供；论文所用代码的公开链接原文未提供。

---

## 论文内容详细总结

### 研究背景与目的

- 等原子比面心立方 CrMnFeCoNi 是典型 Cantor 高熵合金。实验已观察到其 L1₂ 型原子短程有序（ASRO）及 Cr–Cr 回避倾向，但这种有序对残余电阻率 $\rho_0$ 的定量影响未明。
- 既有 KKR-CPA 计算值比实验电阻率低约 35%；含 Al 高熵合金的短程有序可使 $\rho_0$ 改变 20%–80%。作者检验全 3d 元素构成的 CrMnFeCoNi 是否也具有类似敏感性，以及 ASRO 能否解释计算与实验的差距。

---

### 研究方法

- 采用第一性原理浓度波分析（CWA），从等原子比无序 A1 结构出发，以化学稳定性矩阵在 X 点的最低本征值确定 L1₀ 与 L1₂ 候选有序结构及两亚晶格占位。分别考虑低温亚铁磁（FM）和以无序局域磁矩（DLM）模型描述的顺磁（PM）状态。
- 自洽计算使用 SPR-KKR、局域密度近似（LDA）、实验晶格常数 3.5991 Å、48 × 48 × 48 的 $k$ 点网格和 $l_{\max}=3$；随后以全相对论 LDA-CPA 计算两结构，使用 L1₀ 的 48 × 48 × 34 与 L1₂ 的 34 × 34 × 34 网格。
- 以连续参数 $\eta$ 从 A1 无序态（$\eta=0$）插值到 CWA 预测的有序占位（$\eta=1$）。后者仍是部分占位，并非各亚晶格仅含单一元素的完全长程有序。
- 用含 CPA 组态平均和顶角修正的 Kubo–Greenwood 公式计算电导张量，输运计算采用 150 000 个 $k$ 点和 $l_{\max}=4$。再结合 Bloch 谱函数、费米速度、分波态密度及散射相移分析机制，并通过合金类比模型估计静态晶格位移（SLD）的作用。

---

### 主要结果

- FM 的 L1₀ 态中，随 $\eta$ 增加，总能单调降低；$\eta=0$ 时 L1₀ 比 A1 低约 3 meV/atom，原因是两亚晶格带来的额外磁自由度。PM 的 A1、L1₀ 和 L1₂ 在 $\eta=0$ 时总能在 $1\times10^{-7}$ Ry/atom 精度内相同。
- FM L1₀ 从 $\eta=0$ 到 1，$\rho_0$ 由 66.5 增至 68.8 μΩ cm，约在 $\eta=0.5$ 饱和；纯 ASRO 贡献约 2 μΩ cm，即 3.4%。PM 中 ASRO 增幅为 1.6%。A1 FM 到 L1₀ FM 的约 10% 总增幅主要来自磁重排，而非有序本身。
- A1 FM 电阻率为 62.4 μΩ cm，A1 PM 为 66.9 μΩ cm，相变使其上升约 7%。SLD 在各种结构中再增加约 4%（FM）或 2.5%（PM）。计算所得各态均低于实验的 101–105 μΩ cm；最有序 FM L1₀ 的 68.8 μΩ cm 与实验仍差 32–36 μΩ cm。
- L1₀ FM 完全有序端点的纵向电阻率为 $\rho_{xx}=\rho_{yy}=66.5$、$\rho_{zz}=73.3$ μΩ cm，约 10% 各向异性；PM 对应为 66.3 与 71.3 μΩ cm，约 8%。$\eta=0$ 和立方 L1₂ 的纵向分量差异低于 3%。
- 有序前后，费米能级的 sp 态密度变化低于 3%，总态密度约变 5%；L 点谱峰给出的寿命均约 15 fs。$sp$ 权重大于 0.1 的少数态仅占费米能级谱权重约 13%，却承担约 45% 的电流代理量。
- 相邻 3d 元素间的单位核电荷差通过 Friedel 屏蔽主要落在局域 d 通道：A1 FM 中逐对的 d 通道贡献为 89%–98%。排序所引起的单个散射体相移变化一般远小于元素间相移差；sp 输运态因而基本不受影响。

---

### 讨论与结论

- 作者将电阻率对 ASRO 不敏感归因于 sp 能带受到“保护”：化学差别主要由 d 通道吸收，而载流较快的 sp 混合态、散射寿命和速度几乎不变。有限的电阻率变化主要与费米能级态密度降低相符。
- 对同一 d 行、且各元素在费米能级都有 d 共振的合金，作者预计此机制也适用，包括 Cantor–Wu 系列。Al 等 sp 区元素或来自不同 d 行的元素可能把相移差推入 sp 通道，使电阻率对成分和有序化更敏感。此项跨合金推广是论文的机制预期，不是对所有合金逐一计算的结果。
- 即使加入 ASRO、磁态和 SLD，理论值仍显著低于实验；作者认为需要本模型之外的机制，但本文未确定其具体来源。

---

## 章节翻译

### 摘要

高熵合金中的原子短程有序（ASRO）会改变残余电阻率 $\rho_0$ 等可观测量。我们利用第一性原理浓度波分析，确定 Cantor 合金 CrMnFeCoNi 中最可能出现的 ASRO，并通过 Kubo–Greenwood 形式体系，计算预测的 L1₀ 和 L1₂ 有序结构的 $\rho_0$ 随连续原子有序参数变化的关系。ASRO 使 $\rho_0$ 在亚铁磁相中提高 3.4%，在顺磁相中提高 1.6%，远小于计算值与测量值之间 32–36 μΩ cm 的差距。这种不敏感性反映了 Friedel 屏蔽：连续 3d 元素之间的电荷差几乎完全局限于局域化 d 通道，而 sp 态基本不变。我们预计，单行 d 区元素合金（包括 Cantor–Wu 系列）也存在这种 sp 能带保护；当 Al 等 sp 区元素迫使差异进入 sp 通道时，这种保护便会失效，使 $\rho_0$ 对成分和有序化都变得敏感。

---

本稿为 Scripta Materialia 无章节子标题的短文。摘要之后，正文开头至“这些能量上有利的有序结构”一段为引言；其后从浓度波分析、计算设置到电导公式为方法与初步结果；接续至“最后，我们将输运计算扩展”以及图 4 的部分为结果与讨论；以“In summary”开头的末段为结论。以下按原文顺序连续翻译全部正文。

高熵合金（HEAs）形成单相固溶体，部分归因于近乎最大的构型熵降低了吉布斯自由能 [1]。自 Cantor 等人的开创性工作 [2] 以来，CrMnFeCoNi 一直是典型的面心立方（fcc）高熵合金。五种元素以相同原子浓度（$c_\alpha=20\%$）存在，可能的排列方式众多，这使得用超胞密度泛函理论（DFT）计算对随机组态求平均，即便采用特殊准随机结构，也需要很高的计算成本 [3, 4]。相干势近似（CPA）等有效介质理论提供了高效的替代方案 [3, 5-11]。然而，实验与建模都已表明，位点占据完全随机只是一种理想化假设：CrMnFeCoNi 及相关 Cantor–Wu 合金中存在 ASRO [12-15]，更广泛的高熵合金中也存在 ASRO [16-19]。尤其是，近期原子探针断层成像研究直接证明了 CrMnFeCoNi 中存在 L1₂ 型 ASRO，并具有明显的 Cr–Cr 回避倾向 [12]。在 CPA 框架内，可以通过非局域扩展中的 Warren–Cowley 参数表征 ASRO [20-22]，也可以通过具有位点特定浓度的部分有序超晶格结构（fcc 的 L1₀、L1₂）来表征 [23-25]。

对于 CrMnFeCoNi，计算表明 L1₀ 或 L1₂ 有序化在能量上更有利 [26, 27]。这种原子关联可以影响力学及其他性质 [28-30]，但其对 CrMnFeCoNi 残余电阻率 $\rho_0$ 的定量影响尚未得到评估。在含 Al 高熵合金中，ASRO 会使 $\rho_0$ 改变 20%–80% [29, 31]；但考虑到 KKR-CPA 对测得的 $\rho_0$ 持续低估约 35% [3, 10]，完全由 3d 元素组成的 Cantor 合金是否也有类似表现仍是开放问题。本文从第一性原理出发，构建 CrMnFeCoNi 在亚铁磁（FM）和顺磁（PM）相中能量上有利的 L1₀ 和 L1₂ 有序组态，并通过 Kubo–Greenwood 形式体系计算 $\rho_0$ 随连续有序参数 $\eta$ 的变化，以回答这一问题。

这些能量上有利的 CrMnFeCoNi 有序组态由第一性原理浓度波分析（CWA）获得 [26, 27, 32, 33]。CWA 检验等浓度 $c_\alpha=20\%$（$\alpha\in\{\mathrm{Cr,Mn,Fe,Co,Ni}\}$）均匀无序 fcc 假设结构（Strukturbericht A1，图 1a）的稳定性。位点占据的变化表示为浓度波

$$
c_{i\alpha}=c_\alpha+\sum_{\mathbf{k}}\Delta c_\alpha(\mathbf{k})e^{i\mathbf{k}\cdot\mathbf{R}_i}.
$$

当化学稳定性矩阵 $[\beta^{-1}C^{-1}_{\alpha\alpha'}-S^{(2)}_{\alpha\alpha'}(\mathbf{k})]$ 的最低本征值在 X 点过零时，便发生 L1₀（图 1b）或 L1₂（图 1c）有序转变（图 1d）。这里，$S^{(2)}_{\alpha\alpha'}(\mathbf{k})$ 是有效成对相互作用 $S^{(2)}_{i\alpha j\alpha'}=\partial^2\Omega/\partial c_{i\alpha}\partial c_{j\alpha'}$ 的傅里叶变换（图 1e），而 $C^{-1}_{\alpha\alpha'}=\delta_{\alpha\alpha'}/c_\alpha$ 表示理想混合熵对自由能的贡献 [32]。本征值消失处的波矢 $\mathbf{k}_{\mathrm{ord}}$ 确定有序结构，化学极化量 $\Delta c_\alpha$ 则确定亚晶格占位。

自洽场（SCF）计算采用 Vosko、Wilk 和 Nusair 参数化的局域密度近似（LDA）[34]，固定实验晶格常数 $a_{\mathrm{lat}}=3.5991$ Å [3]，布里渊区积分使用 48 × 48 × 48 的 $k$ 点网格，角动量截断为 $l_{\max}=3$。这些 SCF 计算在 SPR-KKR 程序包中以自旋极化、标量相对论形式实现 [35-38]。CWA 预测的亚晶格浓度列于表 1。

CrMnFeCoNi 的居里温度约为 40 K [30, 39]，因此我们将亚铁磁状态视为低温极限，并另外计算以无序局域磁矩（DLM）图像描述的顺磁相 [40-42]，用于比较；这样做也考虑到测量得到的残余电阻率在 100 K 以下几乎不变（最多上升 2%）[10, 43]。在两种磁态中，CWA 都得到两个稳定性相同的候选结构：原始四方 L1₀ 结构（空间群 123，$a=b=2.5449$ Å，$c=3.5991$ Å，Wyckoff 位置 1a 和 1d）以及有序立方 L1₂ 结构（空间群 221，$a=b=c=3.5991$ Å，Wyckoff 位置 1a 和 3c）[26]。两者都是与 A1 成分相同、与 fcc 相容的超结构，仅亚晶格分辨浓度不同；这些浓度列于表 1，并以饼图示于图 1b、c。使用这些浓度 $c_{i\alpha}$，我们分别以 48 × 48 × 34（L1₀）和 34 × 34 × 34（L1₂）的 $k$ 点网格重新收敛 LDA-CPA 基态，保持与 A1 布里渊区（BZ）相同的采样密度。这项重新收敛及后续全部输运计算均在全相对论理论层次上进行。

在两种磁态中，我们用 $c_{i\alpha}(\eta)=(1-\eta)c_\alpha+\eta c^{\mathrm{ASRO}}_{i\alpha}$ 参数化 A1 参考态与 CWA 端点之间的有序化，使体系从 $\eta=0$ 的完全无序平滑变化至 $\eta=1$ 的 CWA 预测有序极限。CWA 端点（$\eta=1$）不同于每个亚晶格仅由一种元素占据的完全周期性长程有序（LRO）[27]。图 2 展示 FM 相中 L1₀ 结构随 $\eta$ 的变化。

随着 $\eta\to1$，总能单调下降（图 2a），表明 CWA 预测的 L1₀ 有序化在 FM 相中热力学上有利。在另一端点 $\eta=0$，尽管 Wyckoff 位置 1a 和 1d 的浓度均相同（$c_{i\alpha}=20\%$），L1₀ 假设结构的能量仍比 A1 参考态低约 3 meV/atom。这一差值反映两亚晶格结构额外的磁自由度：1a 和 1d 位点的磁矩可以不同，从而达到能量更低的亚铁磁态。对 $\eta=0$ 的 A1、L1₀ 和 L1₂ 进行顺磁（DLM）计算，所得总能在 $1\times10^{-7}$ Ry/atom 的数值精度内相同，证实差值起源于磁性。

L1₀ FM 态是亚铁磁态，两个亚晶格上的 Mn 磁矩反平行排列 [27]，这也见于 Cantor 合金家族 [30]。随着 1a 位点变得富 Mn、Cr–Mn 交换 [27] 占主导，1a 位点上的 Cr 磁矩在 $\eta\approx0.4$ 附近反转（图 2c），总磁化强度则随 $\eta$ 线性下降（图 2b）。

A1 以及 $\eta=0$、1 的 L1₀ 的自旋求和态密度（DOS）及其轨道分解（图 2d），在费米能级 $E_F$ 以下几乎无法区分。在 $E_F$ 以上约 1.2 eV 的肩部附近，三者存在明显差异，但只发生在 d 通道。$E_F$ 处的 sp 态密度几乎不随 $\eta$ 改变（变化低于 3%，而 $E_F$ 处总态密度变化约 5%），因此 ASRO 主要影响 d 通道。

图 2e 给出 $\eta=1$ 时每种元素在 L1₀ 两个亚晶格上各能带的自旋分辨相移 $\delta_l(E_F)$。d 能带共振位于费米能级（$E_F$）以下，使 d 相移绝对值超过 $\pi/2$，平均约为 2.4 rad。$E_F$ 处非共振的 s、p 能带相移要小得多，$|\delta_s|\approx0.5$ rad，$|\delta_p|\approx0.08$ rad。在完全有序端点（$\eta=1.0$），Fe、Co 和 Ni 在所有通道中的位点间差异均小于 45 mrad，至多是 d 相移绝对值的 1.5%，所以这些通道基本不受扰动。Mn 和 Cr 的差异较大：在两个自旋通道中符号相反，d 通道最大达 0.9 rad；这反映的是两亚晶格上的反平行磁矩，而非化学有序。

我们以电阻率张量 $\rho_{\mu\nu}=(\sigma^{-1})_{\mu\nu}$ 对角元的平均值，计算多晶平均纵向残余电阻率 $\rho_0=(\rho_{xx}+\rho_{yy}+\rho_{zz})/3$。电导率张量采用 SPR-KKR 中实现的 Kubo–Greenwood 形式体系 [3, 10, 29, 44-46]：

$$
\sigma_{\mu\nu}=\frac{\hbar}{\pi N\Omega_{\mathrm{BZ}}}\operatorname{Tr}\left\langle j_\mu\operatorname{Im}G^+(E_F)j_\nu\operatorname{Im}G^+(E_F)\right\rangle_{\mathrm{CPA}},\tag{1}
$$

其中 $\mu,\nu\in\{x,y,z\}$，$j_\mu$ 是 $\mu$ 方向的相对论性电流密度算符，$A(\mathbf{k},E_F)=-(1/\pi)\operatorname{Im}G^+(\mathbf{k},E_F)$ 是 Bloch 谱函数；在 $E_F$ 处，它表征布里渊区体积 $\Omega_{\mathrm{BZ}}$ 内的费米面及经无序展宽的准粒子寿命。我们使用 150 000 个 $k$ 点收敛电流矩阵元，并将输运计算的角动量截断提高到 $l_{\max}=4$。尖括号 $\langle\cdot\rangle_{\mathrm{CPA}}$ 表示对置换无序的 CPA 组态平均，其中包含相应的顶角修正 [47, 48]。

无序 A1 相的电阻率低于 L1₀（$\eta=0$）参考态（图 2f）。我们将这一差值归因于两亚晶格结构中反平行 Mn 磁矩造成的自旋无序散射。随着体系趋近 CWA 预测的 L1₀ ASRO，$\rho_0$ 从 $\eta=0$ 时的 66.5 μΩ cm 升至 $\eta=1$ 时的 68.8 μΩ cm，在 $\eta\approx0.5$ 附近达到饱和。这一 ASRO 贡献 $\Delta\rho^{\mathrm{ASRO}}_0\approx2$ μΩ cm，小于此前 A1 至 L1₀（$\eta=0$）的磁性跃升（约 4 μΩ cm），并比含 Al 高熵合金中报道的 ASRO 引起的 21 μΩ cm 变化小一个数量级 [29]。因此，从均匀无序晶胞到有序晶胞，FM 态电阻率增加的主要原因是 Mn 磁矩的亚铁磁排列，而不是 ASRO。即使将两项贡献相加，最有序亚铁磁组态的 68.8 μΩ cm 与测得的 101–105 μΩ cm [10, 30, 43] 之间仍有 32–36 μΩ cm 的巨大差距。

以下借助弛豫时间近似下的半经典 Boltzmann 输运解释这一结果。在该框架中，各向同性电导率为 $\sigma=(e^2/3)\langle v_{\mathbf{k}}^2\rangle_{E_F}\langle\tau_{\mathbf{k}}\rangle_{E_F}g(E_F)$ [29, 49, 50]；$\langle v_{\mathbf{k}}^2\rangle_{E_F}$ 和 $\langle\tau_{\mathbf{k}}\rangle_{E_F}$ 分别是速度平方和寿命的费米面平均 $\langle\cdot\rangle_{E_F}$。寿命 $\tau_{\mathbf{k}}$ 由源自 CPA 自能的化学无序展宽 $\Delta E\sim\hbar/\tau_{\mathbf{k}}$ 决定。

图 3a–c 给出 FM 相中 A1 以及 $\eta=0$ 和 1 的 L1₀ 的 Bloch 谱函数（BSF）。由于 L1₀ 晶胞体积为 A1 的两倍，其布里渊区减半，能带发生折叠。为与 A1 参考态直接比较，L1₀ 的 BSF 使用母相 A1 fcc 的高对称点标记（Γ、X、K、L、W），而非标准 L1₀ 布里渊区标记。$\eta=1$ 时最明显的新特征，是 Γ 与 X 之间及 Γ 与 K 之间出现避免交叉；它源于两个不等价亚晶格造成的平移对称性改变 [51, 52]。图 3d 比较了 $\eta=0$ 和 1 的 L1₀ 在高对称点 L 和 W 处 BSF 随能量的变化；选取这两点是因为它们在 $E_F$ 附近有显著峰值。在 L 点，对 BSF 峰作 Lorentzian 拟合得到 $\tau_{\mathbf{k}=L}\approx15$ fs，$\eta=0$ 和 1 时相同，说明散射率对 ASRO 不敏感。

图 3e 展示 $\eta=0$ 和 1 时速度模 $|\mathbf{v}_{\mathbf{k}}|=\sqrt{\sum_\mu v_\mu^2(\mathbf{k},E_F)}$ 在 $k_z=0$ 的截面，其中 $v_\mu(\mathbf{k},E_F)\approx A_{j_\mu}(\mathbf{k},E_F)/[-eA(\mathbf{k},E_F)]$ 由相对论性电流密度算符 $j_\mu=-ec\alpha_\mu$ 的期望值得到：

$$
A_{j_\mu}(\mathbf{k},E_F)=-\frac{1}{\pi}\operatorname{Im}\operatorname{Tr}\left[j_\mu G^+(\mathbf{k},E_F)\right].\tag{2}
$$

X 点附近最内侧的两个片层的费米速度达到约 $0.5\times10^6$ m/s；整个费米面还有速度约为其一半的广泛背景，以及 Γ 点附近速度约 $0.3\times10^6$ m/s 的另一片层。$\eta=0$ 和 1 的速度大小一致，仅在 $\eta=1$ 时片层半径略微缩小。这与图 3f 分辨出的四个片层相符：一个几乎跨越整个布里渊区且强烈弥散的大轮廓 [8]、每个 X 点附近的两个锐利口袋，以及 Γ 点附近的一个较小环。

为识别载流态，图 3g、h 展示 $k_z=0$ 费米面截面上 s 和 p 的谱权重 $f_l=A_l(\mathbf{k},E_F)/A(\mathbf{k},E_F)$。由于奇宇称电流算符的在位矩阵元满足 $\Delta l=\pm1$ 的选择定则，正是 sp 混合将 $E_F$ 处以 d 特征为主的态耦合至电流。该混合集中于 X 点附近的两个最内侧片层，与速度峰位置一致，并且同样对 $\eta$ 不敏感；即便在此处，$f_{sp}$ 也仅达到约 0.15–0.3，因此费米面各处仍以 d 特征占主导。图 3i 给出 $k_z=0$ 平面上 $f_{sp}=f_s+f_p$ 与 $|\mathbf{v}_{\mathbf{k}}|$ 的相关性，表明 sp 混合决定载流子速度：在 $\eta=0$ 与 1 时，$|\mathbf{v}_{\mathbf{k}}|$ 都随 $f_{sp}$ 单调增加。按 $f_{sp}$ 对 $k_z=0$ 的态排序，$f_{sp}>0.1$ 的少数态仅占 $E_F$ 处谱权重的约 13%，却承担约 45% 的电流代理量 $A(\mathbf{k},E_F)v_{\mathbf{k}}^2$；$\eta=0$ 与 1 均是如此。

因此，在 Boltzmann 框架内，既然 $|\mathbf{v}_{\mathbf{k}}|$ 与 $\tau_{\mathbf{k}}$ 基本不随有序化变化，$\rho_0$ 因有序化产生的变化必然来自态密度 $g(E_F)$。对纯 sp 能带，其比值标度为 $\rho_{\eta=1}/\rho_{\eta=0}=g_{sp,\eta=0}(E_F)/g_{sp,\eta=1}(E_F)=1.028$；而总态密度给出 $g_{\eta=0}(E_F)/g_{\eta=1}(E_F)=1.048$。$\eta=1$ 时态密度较低，与图 3f 中片层半径缩小所显示的费米面缩小相符。态密度变化与 Kubo–Greenwood 计算得到的 3.4% 变化一致。

图 3j 比较了控制漫散射的两种 $E_F$ 处相移差，它们由图 2e 的自旋分辨相移构成。无序合金在 $\eta=0$ 时，同一亚晶格上不同元素之间的差 $|\delta_l^i-\delta_l^j|$，类似于文献 [3] 所讨论的 d 能带中心失配，并决定化学无序散射强度。最大的元素间差异出现在 d 通道，达到 0.3–1.1 rad。各散射体因有序化引起的变化 $|\delta_l(\eta=1)-\delta_l(\eta=0)|$ 在所有通道均低于 0.03 rad，惟 Cr 和 Mn 的 d 通道例外：磁矩重排（图 2c）使其变化最大达到 0.19 rad。平均而言，在所有通道中，有序化引起的变化比元素间差异小一到两个数量级。因此，有序化基本只是重新排列几乎不变的散射体；确实发生的有限变化源于磁性，且局限于 d 通道。

我们认为，这种对 ASRO 不敏感的微观起源可由 Friedel 求和定则解释 [50, 53]。对于两个相邻的 3d 元素 $\alpha$ 和 $\alpha'$，额外的核电荷 $\Delta Z=1$ 必须在晶胞内得到屏蔽，因此有 [54, 55]：

$$
\Delta Z=\frac{2}{\pi}\sum_l(2l+1)\Delta\delta_l^{\alpha\alpha'}(E_F),\tag{3}
$$

其中 $\Delta\delta_l^{\alpha\alpha'}(E_F)=\delta_l^\alpha(E_F)-\delta_l^{\alpha'}(E_F)$ 为相移差。屏蔽在不同通道中的分配与 $E_F$ 处单个位点的分波态密度 $n_l(E_F)=(2l+1)/\pi\,[d\delta_l(E)/dE]_{E_F}$ 成正比 [56]。（式 (3) 以非相对论形式书写。）按通道分解无序 A1 结构的元素间相移差（表 2）表明，从 Cr 至 Ni 每一对相邻元素的 $\sum_l(2l+1)\Delta\delta_l(E_F)$ 中，d 通道占 89%–98%。在 $\eta=0$ 和 1 时，L1₀ 两个亚晶格上的 sp 相移差都同样很小，d 通道贡献 86%–98%。

相比之下，含 Al 高熵合金 [29, 31, 57, 58] 对 ASRO 明显更敏感。Al 在 $E_F$ 处没有 d 共振，因此它与 3d 成分之间的电荷转移必须经由 sp 通道屏蔽 [58, 59]，使 $\Delta\delta_s$ 和 $\Delta\delta_p$ 增大，并让 sp 输运暴露于结构无序。第一性原理计算发现，含 Al 合金 AlTiVCr、AlTiVNb 和 AlTiCrMo 都具有强烈的 ASRO 敏感性：有序化使其 $\rho_0$ 分别提高约 80% [31]、20% 和 40% [29]。实验观察到，NiCrAlFe 合金中的 ASRO 使 $\rho_0$ 提高 11% [57]。对 Al$_x$CoCrFeNi 的第一性原理 Kubo–Greenwood 计算表明，随着 Al 含量增加，$\rho_0$ 提高约 60% [58]；该研究将此归因于 sp–d 杂化，它使过渡金属有效价变负，并减少导电态。该杂化图像与本文的相移图像描述的是同一个效应。根据式 (3) 的 Friedel 求和定则，有效价等于被屏蔽的电荷，因而等于相移之和；因此，Al 迫使电荷进入 sp 通道，会同时表现为散射中较大的 $\Delta\delta_{sp}$ 和杂化后较低的 sp 态密度。当元素间差异局限于局域化 d 通道时，如全 3d 元素 Cantor 合金，$\rho_0$ 对成分和有序化都很稳健。当 sp 区元素把差异转移到快速的 sp 通道时，$\rho_0$ 就会对成分敏感，如 Al$_x$CoCrFeNi [58]；也会对有序化敏感，如上文讨论的含 Al 合金 [29, 31, 57]。

最后，我们将输运计算扩展到 L1₂ 结构和 PM 相。在这里，原子尺寸失配造成的静态晶格位移（SLD）通过合金类比模型 [60] 引入。元素分辨位移取自 Mu 等人 [3]，$u_{\mathrm{rms},\alpha}=\sqrt{3\pi/8}\langle|\Delta u_\alpha|\rangle$，分别为 $u_{\mathrm{rms,Cr}}=0.077$ Å、$u_{\mathrm{rms,Mn}}=0.056$ Å、$u_{\mathrm{rms,Fe}}=0.048$ Å、$u_{\mathrm{rms,Co}}=0.037$ Å、$u_{\mathrm{rms,Ni}}=0.031$ Å。

图 4 汇总了 FM 和 PM 两相中 A1、L1₀、L1₂ 的 $\rho_0$，并分别考虑有无 SLD。FM 至 PM 的转变使 A1 的 $\rho_0$ 从 62.4 μΩ cm 增至 66.9 μΩ cm（7%）；SLD 在所有结构中进一步增加约 4%（FM）和 2.5%（PM）。在 FM 相中，A1 → L1₀（$\eta=1$）使 $\rho_0$ 达到 68.8 μΩ cm（比 A1 高 10%），其中主要是磁性作用，而非结构作用（见图 2f 的 $\eta$ 扫描）；ASRO 本身仅增加约 2 μΩ cm。PM L1₀ 的 68.0 μΩ cm 仅比 A1 PM 高 1 μΩ cm；L1₂ 在两种磁态下都位于 A1 与 L1₀ 之间。

完全有序端点（$\eta=1$）的四方 L1₀ 结构产生明显的纵向各向异性。FM 相中 $\rho_{xx}=\rho_{yy}=66.5$ μΩ cm，$\rho_{zz}=73.3$ μΩ cm（各向异性 10%）；PM 相中相应数值为 $\rho_{xx}=\rho_{yy}=66.3$ μΩ cm 和 $\rho_{zz}=71.3$ μΩ cm（各向异性 8%）。在 $\eta=0$ 及立方 L1₂ 结构中，纵向分量的差异小于 3%。在 CrMnFeCoNi 中实验观察到的 L1₂ 型 ASRO [12]，产生了两种有序化增幅中较小的一种（比 A1 FM 高 6%，而 L1₀ 高 10%）。所有组态的电阻率都远低于测得的 101–105 μΩ cm [10, 30, 43, 58]。这一持续存在的差距因此指向当前建模框架未描述的机制。

总之，我们的第一性原理计算表明，CWA 预测的 ASRO 使 CrMnFeCoNi 的 $\rho_0$ 在 FM 相中增加 3.4%（$\Delta\rho_0\approx2$ μΩ cm），在 PM 相中增加 1.6%。FM 相中 A1 至 L1₀ 更大的 10% 跃升主要由磁重排引起，而非 ASRO。对于 Cr 至 Ni 的相邻元素，Friedel 求和定则使单位电荷差几乎完全在局域化 d 通道中得到屏蔽，所以化学重排主要扰动 d 态。因此，$\rho_0$ 对 ASRO 的敏感性由有序化影响 sp 通道的程度决定。由同一行 d 区元素构成、且所有组分在 $E_F$ 处均有 d 共振的合金家族，会将差异保留在 d 通道中，预计也具有这种 sp 能带保护，包括 Cantor–Wu 系列。相比之下，Al 等 sp 区元素 [29]，或来自不同行 d 区元素的组分，会将差异推入 sp 通道，使 $\rho_0$ 对成分和有序化都变得敏感。

---

## 结果与讨论子标题翻译

原文没有结果与讨论章节的子标题。

---

## 图表题翻译

图 1：与 CWA 有关的数据。（a）CrMnFeCoNi 的均匀无序 Strukturbericht A1（即 fcc）结构，Wyckoff 位置 4a 的单一亚晶格以相同概率容纳 Cr、Mn、Fe、Co 或 Ni 各种置换元素（颜色编码的饼图）。（b）具有两个亚晶格（Wyckoff 位置 1a 和 1d）的原始四方 L1₀ 结构，以及（c）具有两个亚晶格（1a 和 3c）的有序立方 L1₂ 结构。CWA 预测各组分在每个亚晶格上的最稳定浓度，以颜色编码饼图表示，并作为残余电阻率计算的输入。（d）化学稳定性矩阵 $[\beta^{-1}C^{-1}_{\alpha\alpha'}-S^{(2)}_{\alpha\alpha'}(\mathbf{k})]$ 的本征值，以及（e）在 FM 相、$T=500$ K 下由 CWA 获得的傅里叶变换有效成对相互作用 $S^{(2)}_{\alpha\alpha'}(\mathbf{k})$。稳定性矩阵在 X 点的最小本征值表明体系优先形成趋向 L1₀ 和 L1₂ 结构的 ASRO。

图 2：L1₀ FM 结构的电子结构和输运性质随有序参数 $\eta$ 的演化。无序 fcc CPA 参考态（A1）以星号标示。（a）L1₀ 与 A1 结构之间每原子的 SCF 总能差 $\Delta E_{\mathrm{tot}}=E-E^{(\mathrm{A1})}_{\mathrm{tot}}$。（b）总磁化强度。（c）Cr（青色）、Mn（粉色）、Fe（橙色）、Co（蓝色）和 Ni（灰色）的位点及元素分辨磁矩；实心圆表示 1a 位点，实心方块表示 1d 位点。（d）A1（点线）、$\eta=0$ 的 L1₀（点划线）和 $\eta=1$ 的 L1₀（实线）的能带分辨态密度和总态密度；在 $E_F$ 处，s、p 投影分量几乎不随 $\eta$ 变化，而 1.2 eV 附近肩部的差异局限于 d 通道。（e）$\eta=1$ 时 L1₀ 的 1a 和 1d 亚晶格上各元素 s、p、d 能带的自旋分辨相移 $\delta_l(E_F)$；实心和空心符号分别表示 $\sigma=\uparrow$ 和 $\sigma=\downarrow$。使用全相对论势，在自旋极化标量相对论模式下评价相移。纵轴分段，各段采用不同刻度。（f）残余电阻率 $\rho_0$。

图 3：Bloch 谱函数（BSF）$A(\mathbf{k},E)$：（a）无序 A1 FM 参考态、（b）$\eta=0$ 的 L1₀ FM 和（c）$\eta=1$ 的 L1₀ FM，均沿 fcc 高对称路径绘制。L1₀ 晶胞加倍造成布里渊区折叠，产生折叠能带；$\eta=1$ 时，Γ 与 X 之间以及 Γ 与 K 之间出现避免交叉。（d）对于 $\eta=0$（点划线）和 $\eta=1$（实线）的 L1₀，在高对称点 L 和 W 处，$A(\mathbf{k},E)$ 随能量变化，突出显示 L 点 Lorentzian 峰宽保持不变。（e）$\eta=0$（左上）和 $\eta=1$（右下）的 L1₀ 在 $k_z=0$ 的费米速度大小 $|\mathbf{v}_{\mathbf{k}}|$ 截面。（f）L1₀ 结构在 $\eta=0$（左上）和 $\eta=1$（右下）时的费米面截面 $A(\mathbf{k},E_F)|_{k_z=0}$。（g）和（h）分别表示 s 和 p 能带的谱权重比例 $f_l=A_l(\mathbf{k},E_F)/A(\mathbf{k},E_F)|_{k_z=0}$，其中 $A=\sum_{l\leq f}A_l$；比较 L1₀ FM 的 $\eta=0$（左上）与 $\eta=1$（右下）组态。（i）$E_F$ 和 $k_z=0$ 处的 sp 权重 $f_{sp}=f_s+f_p$ 与速度 $|\mathbf{v}_{\mathbf{k}}|$ 的相关性。（j）$E_F$ 处的自旋分辨相移差；展示两个亚晶格，但不作区分。圆点表示 $\eta=0$ 无序合金同一亚晶格上所有十对元素的元素间差 $|\delta_l^i-\delta_l^j|$，实心表示 $\sigma=\uparrow$，空心表示 $\sigma=\downarrow$，配对颜色与图 1e 相同。三角形表示每种元素的有序化引起的变化 $|\delta_l(\eta=1)-\delta_l(\eta=0)|$，颜色与图 2c 相同，向上指 $\sigma=\uparrow$，向下指 $\sigma=\downarrow$。$\eta=1$ 时 1a 亚晶格上的 Fe 是权重为零的 CPA 组分，因此省略。

图 4：所有考虑结构（A1、L1₀、L1₂）和磁态（FM、PM）的多晶平均残余电阻率 $\rho_0$；加入静态晶格位移（SLD）[3] 后，与 101–105 μΩ cm 的实验测量值 [10, 30, 43] 比较。

---

表 1：CWA 预测的 FM 和 PM 状态下 L1₀ 与 L1₂ 有序结构中，按位点和元素分辨的浓度 $c_{i\alpha}$。无序 A1 参考态的所有位点均有 $c_\alpha=0.2$。接近 0 或 1 的数值反映 CWA 预测的最大亚晶格亲和性，而非实际空位。

表 2：在 A1、FM 状态下，按 s、p、d、f 通道分解的相邻 3d 元素对单个位点 Friedel 求和。各项对两个自旋通道求和，每个自旋通道按式 (3) 使用 $1/\pi$。对所有元素对，求和均小于单位电荷差 $\Delta Z=1$；余量由周围的有效介质屏蔽。
