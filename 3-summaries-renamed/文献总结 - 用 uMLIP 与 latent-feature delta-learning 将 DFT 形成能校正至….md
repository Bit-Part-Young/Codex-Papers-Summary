# 文献总结 - 用基础机器学习原子间势与潜特征 delta 学习将 DFT 形成能校正至实验精度 - 2026

## 文献基本信息

- 英文原文标题：Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning
- DOI 链接：原文未给出正式论文 DOI；数据计划发布 DOI 为 https://doi.org/10.24435/materialscloud:yb-gw
- 作者：Timo Reents, Marnik Bercx, Giovanni Pizzi
- 期刊名称：arXiv 预印本，arXiv:2607.18092v1 [cond-mat.mtrl-sci]
- 投稿 - 返修 - 接收 - 在线发表日期：原文未给出投稿、返修、接收日期；PDF 标注日期为 July 21, 2026；arXiv 记录为 20 Jul 2026
- 数据/代码链接：数据将在论文发表后通过 Materials Cloud Archive 公开，https://doi.org/10.24435/materialscloud:yb-gw；代码将在论文发表后公开。

## 文献总结

### 研究背景与问题

本文关注高通量密度泛函理论（DFT）材料数据库中的热力学稳定性数据，特别是形成能和凸包以上能量。Materials Project、OQMD、AFLOW、Alexandria 和 Materials Cloud three-dimensional crystals database（MC3D）等数据库通常使用 DFT 构建，并将形成能作为筛选稳定或亚稳定材料的重要指标。

作者指出，SCAN、rSCAN、r2 SCAN 等 meta-GGA 泛函通常比 PBE、PBEsol 等 GGA 泛函给出更接近实验的稳定性结果，但大量既有数据库仍主要采用 GGA。这主要是因为 GGA 计算成本较低、社区采用广泛，并且有经过验证的赝势；而 meta-GGA 的大规模验证和赝势生态仍相对不足。GGA 形成能已知存在系统误差，例如双原子气体过结合，以及对含局域电子化合物（如过渡金属氧化物）描述不足。

为改进 GGA 形成能与实验之间的偏差，已有方法包括 Fitted Elemental Reference Energies（FERE）等元素参考态校正。作者强调，经验校正虽能改善形成能，但也会引入额外不确定性，并且在跨数据库比较和机器学习校正时尤其重要。

### 研究目标

本文首先向 MC3D 数据库引入形成能数据，并将其与 Materials Project 和 OQMD 的形成能进行比较，验证不同 DFT 代码、赝势和参数设置下形成能的一致性。随后，作者将 MC3D 的 DFT 形成能与实验形成焓比较，评估 GGA 误差。

文章的核心目标是证明：训练在 r2 SCAN 水平的大型基础机器学习原子间势（foundational MLIPs, fMLIPs），尤其是 PET-OMATPES，可在不额外进行 DFT 计算的情况下显著改善形成能与实验的符合程度。进一步地，作者利用 PET-OMATPES 的潜特征作为结构描述符，在 delta-learning 框架中训练经典机器学习模型，对形成能残差进行进一步校正。

### 数据库比较结果

作者比较了 MC3D、Materials Project 和 OQMD 之间的形成能差异。对于未经经验校正的纯 DFT 形成能，三套数据库之间的一致性较好：四分位距约为 31-42 meV/atom，中位绝对差约为 15-18 meV/atom。MC3D-MP 和 MC3D-OQMD 的分布大体以零附近为中心，而 MP-OQMD 显示约 50 meV/atom 的第二峰。补充分析表明，这些偏差主要来自含氧化合物，反映不同数据库对氧参考态的选择差异。

对于 FERE 校正后的形成能，数据库间差异显著增加。MC3D-MP 与 MP-OQMD 的分布出现更宽的四分位距和双峰特征，主要与 MP 的氧校正方案以及不同数据库所校正元素集合不同有关。MC3D-OQMD 在纯 DFT 与 FERE 校正两种情况下分布变化较小，但 Se 和 Te 含量较高的化合物导致中位数发生约 5 meV/atom 的偏移。作者据此认为，纯 DFT 形成能在不同代码和参数下具有较好可比性，而经验校正是跨数据库形成能差异的重要来源。

### fMLIP 改善 DFT 与实验一致性的结果

作者将 PBE 和 PBEsol 形成能与实验形成焓比较，发现 GGA 形成能相对于实验存在系统性高估，平均绝对误差大于 170 meV/atom，平均误差约为 130 meV/atom。FERE 可将平均绝对误差从约 150 meV/atom 降至约 100 meV/atom，但仍然存在明显误差，并可能引入非平滑性。

作者随后使用训练在 r2 SCAN 水平的 PET-OMATPES 模型，在 DFT 弛豫结构上直接预测形成能。结果显示，零样本 PET-OMATPES r2 SCAN 形成能可将相对于 GGA 的平均绝对误差降低 40% 以上。对于 PBE，未弛豫 MLIP 计算仍有 -28 meV/atom 的小偏差；对于 PBEsol，平均误差降至 0 meV/atom。若使用 PET-OMATPES 进行对称性约束结构弛豫，PBE 起始结构的偏差进一步降至 8 meV/atom，平均绝对误差降至 81 meV/atom；PBEsol 起始结构则变化很小。

作者将这一结果解释为：PBEsol 原本为较准确晶格常数设计，其体积接近 r2 SCAN，因此在 PBEsol 几何上进行 r2 SCAN 水平能量评估已接近最优。这将“PBEsol 几何 + meta-GGA 能量”的 DFT 实践推广到基础 MLIP 时代。

### delta-learning 校正结果

在 PET-OMATPES 已显著改善形成能后，作者进一步训练 Random Forest、Kernel Ridge Regression（KRR）和 Gaussian Process Regression（GPR）模型来学习计算形成能与实验之间的残差。训练目标包括 PBEsol 与实验之间的差值 δΔHfPBEsol，以及零样本 PET-OMATPES r2 SCAN 与实验之间的差值 δΔHfMLIP。

特征方面，作者比较了 Magpie 组成特征和 PET-OMATPES 潜特征。Magpie 特征只依赖组成，因此同一组成的多晶型会获得相同校正；潜特征则包含结构相关信息，可对多晶型给出不同校正。结果表明，潜特征对 KRR 和 GPR 的性能有明显提升，对 Random Forest 则不明显。最佳模型在 δΔHfMLIP 目标上可达到约 49-50 meV/atom 的平均绝对误差，在 δΔHfPBEsol 目标上约为 52 meV/atom。这一误差已接近实验不确定性尺度。

### 相稳定性影响与正则化

作者特别分析了机器学习校正对相对相稳定性的影响，使用“稳定性翻转率”衡量校正前后材料是否从稳定变为不稳定或相反。稳定阈值默认设为 25 meV/atom。结果显示，δΔHfMLIP 目标的翻转率低于 δΔHfPBEsol 目标；而相当一部分翻转来自 PET-OMATPES r2 SCAN 相对于 PBEsol 的物理性改变，而不是后续小模型的任意扰动。

在 KRR 模型中，作者调节正则化参数 α，考察形成能平均绝对误差与稳定性翻转率之间的权衡。较强正则化可显著降低翻转率和跨数据划分的不确定性，但过强正则化会牺牲形成能精度。综合考虑后，作者选择 KRR-LAP-LF 模型，α = 0.1。随机打乱校正值的基线会导致高达 45% 的翻转率，而所选模型翻转率远低于该值，说明模型捕捉到的是有意义的结构-性质关系。

### 与 FERE 方法的比较

作者将最佳 ML 校正方法与 FERE-part 和 FERE-all 两种 FERE 方案比较。三种方法均能改善多数化合物，但 FERE-all 会使 32% 测试化合物变差，平均劣化为 79 meV/atom；FERE-part 会使 22% 化合物变差，平均劣化为 107 meV/atom；ML 校正会使 23% 化合物变差，但平均劣化仅为 37 meV/atom。因此，ML 方法在降低总体平均绝对误差的同时，对少数未改善化合物的损害幅度更小。

### 主要结论

本文建立并验证了 MC3D 数据库的热力学稳定性数据，显示纯 DFT 形成能在 MC3D、MP 和 OQMD 之间总体一致，而经验校正方案是数据库间偏差的重要来源。核心结果是：PET-OMATPES 等基础 MLIP 可在不新增 DFT 计算的情况下，将 GGA 形成能与实验之间的平均绝对误差降低 40% 以上；进一步使用 PET-OMATPES 潜特征和 delta-learning，可将误差降至低于 50 meV/atom，并接近实验不确定性。

作者还证明，潜特征不仅能改善形成能预测，也能在合适正则化下限制对相对相稳定性的扰动。该工作为在既有 GGA 数据库上引入 meta-GGA 级别形成能估计和机器学习残差校正提供了可复现路径。

## 摘要翻译

由高通量密度泛函理论计算整理得到的晶体结构数据库，通常是计算材料发现工作的起点。热力学稳定性数据，例如形成能和凸包以上能量，是指导新材料搜索的重要量，使得对（亚）稳定结构进行筛选成为可能。在这里，我们给出了完全开源、可复现且面向实验的 Materials Cloud three-dimensional crystals database（MC3D）的热力学稳定性。我们将其与另外两个 DFT 数据库，即 Open Quantum Materials Database（OQMD）和 Materials Project（MP），以及实验形成焓进行比较。随后，我们展示了如何利用近期在 r2 SCAN 水平训练的基础机器学习原子间势（MLIPs）（这里我们具体测试 PET-OMATPES）来改善形成能与实验的一致性，在不需要任何额外 DFT 计算的情况下，相对于 GGA 将平均绝对误差降低 40% 以上。我们的结果验证并扩展了将 PBEsol 几何结构与 meta-GGA 能量相结合这一既有实践，使其进入基础 MLIP 时代。最后，我们训练经典机器学习模型，在 delta-learning 框架中进一步校正形成能，其中我们使用基础 MLIP 中信息丰富的潜特征。这些模型进一步将平均绝对误差降低到 50 meV/atom 以下，使其降至与实验不确定性本身相当的数值。值得注意的是，与纯组成特征相比，潜特征结合仔细调节的正则化，同时降低了预测误差，并限制了所学习校正对相对相稳定性的影响。

## 引言翻译

近年来，高通量工作流引擎 [1-6] 使计算材料科学领域的大型数据库得以构建，其中包括 Materials Project（MP）[7, 8]、Open Quantum Materials Database（OQMD）[9, 10]、Automatic FLOW for Materials Discovery（AFLOW）[11-13]、Alexandria [14-16]，以及本文讨论的 Materials Cloud three-dimensional crystals database（MC3D）[17, 18]。这些数据库通常基于密度泛函理论（DFT）[19, 20]，能够以合理的计算成本提供较强预测能力。随着可用晶体结构数据量快速增长 [21, 22]，热力学稳定性已成为材料排序和筛选的重要性质，用于将搜索重点放在更可能在实验条件下存在的化合物上 [23-25]。虽然 SCAN [26]、rSCAN [27] 和 r2 SCAN [28] 等 meta-GGA 泛函已知能够产生与实验参考更一致的稳定性结果 [29-31]，优于 PBE [32] 和 PBEsol [33] 等 GGA 泛函，并且正越来越多地用于近期高通量研究 [15, 34-37]，但上述数据库中的大部分数据仍是在广义梯度近似（GGA）水平计算的，这是由于其计算效率、在社区中的广泛采用，以及经过验证的赝势可用性 [38, 39]；而后者对于 meta-GGA 泛函通常仍然缺失。然而，GGA 形成能已知表现出有限精度，例如由于双原子气体过结合 [40]，以及对含局域电子化合物（例如过渡金属氧化物）描述中的系统误差 [41]。

为了改善 GGA 形成能相对于实验数据的已知局限，已经发展了多种方法。最常见的是元素参考态校正，称为 Fitted Elemental Reference Energies（FERE）[42]，其解决过结合问题并改善 DFT-实验一致性，但代价是引入额外经验性。该方法的不同变体已被多个成熟数据库采用：OQMD 仅对一部分化学元素调整元素参考 [10]，而 MP 使用略有不同的元素子集，并对氧采用依赖环境的校正 [8, 43]，AFLOW 则基于每种元素的局域化学环境拟合校正 [44, 45]。总体而言，经验校正代表了形成能改善与校正本身引入的额外不确定性之间的权衡。当利用机器学习（ML）模型预测 DFT 形成能 [46, 47] 或其相对于实验数据的差异 [48] 时，这种权衡尤其相关，因为 ML 误差可能不那么系统，并且不会像 DFT 那样在相同程度上受益于误差抵消 [49]。

在本文中，我们首先将新引入的 MC3D 数据库形成能与成熟数据库 OQMD 和 Materials Project 中报告的形成能进行比较。由于 MC3D 依赖不同的 DFT 代码和计算参数，该分析有助于 DFT 代码和下游数据库之间的可比性，并扩展既有验证工作 [50]。随后，我们处理改善 DFT 计算形成能与实验之间一致性的挑战。我们展示了如何使既有 GGA 数据库受益于在 meta-GGA 水平训练的基础机器学习原子间势（fMLIPs），在不需要额外 DFT 计算的情况下显著改善热力学稳定性描述。在此基础上，我们展示了如何在 delta-learning 框架中使用此类 fMLIP 的信息丰富的潜特征 [51, 52]，进一步校正 DFT 计算形成能，相对于实验达到低于 50 meV/atom 的 MAE，优于既有方法 [48, 53]。最后，我们考察了在经过仔细调节时，正则化如何在改善形成能精度与控制其对相对相稳定性的影响之间取得平衡。

## 方法翻译

### 计算细节

在这项工作中，我们向 Materials Cloud three-dimensional crystals database [17] 引入形成能；该数据库是一个完全可复现且开源的 DFT 整理数据库，包含三维无机晶体结构，尤其关注实验已知化合物。在这里，我们聚焦于 MC3D 的 PBE-v1 和 PBEsol-v1 版本。

所有 DFT 计算均使用启用 SIRIUS 的 [76] Quantum ESPRESSO version 7.1 [77, 78]，并结合来自 SSSP library [39] 的 PBE [32] 和 PBEsol [33] 赝势（分别为 SSSP PBE Efficiency v1.1.0 和 SSSP PBEsol Efficiency v1.1.0）。当前 MC3D [17] 基于标准 GGA 泛函且不含 Hubbard 校正（在训练 MLIP 时，缺少 Hubbard U 校正实际上可能是有益的，见 [61]）。按照 AiiDA Quantum ESPRESSO 插件 [79] 的默认协议，使用 0.15 Å^-1 的 k 点间距对布里渊区采样。从实验参考结构出发，结构参数和原子位置被弛豫，直到力和能量分别收敛到低于 10^-4 Ry/bohr 和 10^-5 Ry/atom。关于整理过程的细节，读者可参阅原始 MC3D 论文 [17]；关于计算参数选择，可参阅 Nascimento 等 [80]。形成能由收敛的弛豫结果计算得到。

### 参考数据

#### 实验参考

为了评估 DFT 计算形成能的性能，我们使用 Wang 等 [43] 收集并在 matminer 包 [73] 中作为 expt formation enthalpy kingsbury 数据集 [43, 81-87] 发布的实验参考。为了增加实验参考数据的数量和多样性，而这通常是数据驱动研究中的限制因素，我们将其与 Kirklin 等 [10] 使用的实验参考合并，总共得到 2726 个唯一化合物。

在我们的分析中，我们删除满足以下至少一个标准的化合物，以平衡数据质量与数据集大小：

- 该化合物是元素相（新大小：2649）。
- 实验不确定性估计超过 10%。如果没有报告不确定性，则保留该化合物。（新大小：2386）
- DFT 形成能（来自 OQMD）与实验参考相差超过 0.5 eV/atom，仅删除少数离群值。（新大小：2373）
- 该化合物出现在两个数据集中，并且两个来源相差超过 150 meV/atom。（新大小：2356）

由于 MC3D 不包含所有化合物，与实验参考合并后得到 1552 个（PBE）和 1384 个（PBEsol）化合物，其中 1297 个重叠。在将计算数据与实验参考合并时，如果有空间群信息，则使用该信息；否则选择给定组成下能量最低的多晶型。

#### 参考计算数据库

除了与实验数据比较之外，还将 MC3D 形成能与成熟高通量数据库 Materials Project [7, 8] 和 Open Quantum Materials Database [10] 进行比较。我们查询 OQMD v1.5（本地托管）和 MP v2023.11.1，并通过其 ICSD ID 匹配结构。没有匹配 ID 的化合物被排除，并且不进行额外的基于结构的重复检测。MP 和 OQMD 依赖 VASP DFT 代码 [88, 89]，这与使用启用 SIRIUS 的 Quantum ESPRESSO 的 MC3D 不同。这涉及赝势差异，而赝势在结果精度中起核心作用。数据库之间计算参数的差异在补充信息的“Comparison of computational parameters”部分进一步讨论。

### DFT 形成能

为了估计 MC3D 中材料的热力学稳定性，我们计算形成能：

$$
\Delta H_f(A_1^{n_1}\ldots A_N^{n_N}) = E_{\mathrm{tot}}(A_1^{n_1}\ldots A_N^{n_N}) - \sum_{i=1}^{N} n_i \mu(A_i),
$$

其中 $E_{\mathrm{tot}}$ 是由化学元素 $A_1, A_2, \ldots, A_N$ 构成的化合物总能，$n_i$ 是单位胞中由元素 $A_i$ 占据的位点数。化学势 $\mu(A_i)$ 由 MC3D 中最稳定元素多晶型的 DFT 每原子总能给出。该定义在 0 K 下严格成立，而实验形成能通常在标准条件下测得。由此产生的有限温度误差通常为几十 meV/atom 量级，低于 DFT 与实验之间的 MAE，因此被忽略 [10, 43]。如引言所述，GGA 形成能具有已知系统局限。我们在数据库比较中采用 FERE 校正 [42]，并将其作为 ML 校正的基线；拟合过程和与 ML 校正的比较细节分别见补充信息的“FERE corrections”和“Comparison of FERE and ML corrections”部分。没有经验校正的形成能在全文中标记为 Pure DFT。

### 机器学习模型与训练

在与形成能 ML 校正相关的分析中，我们训练 scikit-learn 提供的以下 ML 模型：Random Forest（RF）、Gaussian Process Regression（GPR）和 Kernel Ridge Regression（KRR）。对于后者，我们测试了 Laplacian（LAP）和 RBF 核。所采用的框架遵循 delta-learning 方法，即模型试图学习计算形成能与实验之间的差异，并在成功训练后将其作为校正应用。

含实验参考的 1384 个结构数据集被划分为 80/20 的训练-测试划分。为了估计不确定性，尤其是对于这种较小数据集而言单个材料可能显著改变所学习校正的情况，该划分在 30 个不同随机种子上生成。对于每个训练-测试划分，我们在训练集上进行 5 折交叉验证，以为每个模型找到最佳超参数。此外，最佳超参数集合用于计算每个随机种子的测试误差。在超参数优化和训练-测试划分中使用了分层划分，分层依据为每个结构中的元素数，以确保每个划分覆盖相同的（代表性）一元、二元等结构比例。

使用两组特征：（i）来自 Magpie [72] 的纯组成特征，以及（ii）来自 PET-OMATPES 模型 [63, 64] 潜空间的结构特征，遵循 Chorna 等 [68] 的提取方法。fMLIP 在跨广泛化学范围预测能量和力时学习信息丰富的表征，使其潜空间成为结构描述符的天然来源。我们评估最后一层（LL）特征和骨干（BB）特征。后者在消息传递迭代之后、最终多层感知机（MLP）层之前提取，而这些 MLP 层通常在 MLIP 中用作所谓读出层。由于 BB 特征始终优于 LL 特征，因此在全文中使用 BB 特征，并称为潜特征（LF）。

## 结论对应部分翻译

原文没有单独的 `Conclusions` 章节；以下为正文 `DISCUSSION` 章节的完整翻译，作为结论对应部分。

总之，我们向 MC3D 数据库引入了热力学稳定性数据，并将其与成熟数据库 Materials Project 和 OQMD 进行验证。鉴于 MC3D 基于不同的 DFT 代码、不同赝势和不同计算参数，良好的一致性证实了社区所采用方法的稳健性，并对既有验证工作作出贡献 [38, 50, 75]。该比较还强调，形成能数据库间偏差的主要来源是跨数据库采用的不同经验校正方案。

这项工作的核心贡献是改善形成能与实验的一致性。我们表明，来自基础 MLIP PET-OMATPES 的零样本 r2 SCAN 形成能已经能够在不进行任何额外 DFT 计算的情况下，相对于 GGA 将 MAE 降低 40% 以上。当其与 PBEsol 弛豫几何结构结合时，这种改善尤其显著：由于 PBEsol 晶格常数已经接近 r2 SCAN 的晶格常数，MLIP 弛豫影响很小，并且在 DFT 几何结构上的零样本评估几乎是最优的。这证实并扩展了将 PBEsol 几何结构与 meta-GGA 能量配对的既有实践 [15]，使其进入 fMLIP 范畴。此外，我们还基准测试了直接使用 fMLIP 对原始实验源结构进行结构弛豫（而不是 DFT PBEsol）时的情况，其在形成能方面本质上得到相同精度的结果，并且在实验体积方面的一致性略优于 PBEsol。

在零样本 MLIP 能量之外，我们在 delta-learning 框架中训练经典 ML 模型（KRR、Random Forest 和 GPR），以预测计算或估计形成能与实验之间的残差。使用 PET-OMATPES 的潜特征作为输入，我们的最佳模型对于 PBEsol 和 r2 SCAN 目标均达到低于 50 meV/atom 的 MAE（并且取决于数据划分，可能甚至更低），变得可与实验不确定性本身相比。值得注意的是，与纯组成特征相比，潜特征同时降低了 MAE 和稳定性翻转率。我们进一步表明，仔细调节的正则化能够控制 ML 校正对相对相稳定性的影响。最后，我们将 ML 校正与成熟的 FERE 经验校正进行验证，确认 ML 方法不仅更显著地降低了相对于实验的平均偏差，而且对于少数未能改善的化合物，也限制了劣化幅度。

## 结果/讨论章节子标题翻译

- Comparison with existing databases：与现有数据库的比较
- MLIPs to improve DFT versus experiment：用 MLIP 改善 DFT 相对于实验的一致性
- Learning the correction to improve ΔHfDFT：学习校正以改善 ΔHfDFT
- Balance accurate formation energies with distortion of relative phase stability：在形成能精度与相对相稳定性扰动之间取得平衡
- Comparing with existing approaches：与现有方法的比较
- Discussion：讨论

## 图题和表题翻译

图 1. 不同数据库之间形成能差异的分布：MC3D [17]、Materials Project [7, 8] 和 OQMD [10]。（上排）未校正“纯 DFT”形成能的差异。（下排）使用 FERE 方法进行经验校正后的数据库形成能差异。图例中给出了不同统计量：观测数 $N$、四分位距 IQR（$Q_1-Q_3$，其中 $Q_1$ 是第一四分位数，即 25% 百分位，$Q_3$ 是第三四分位数，即 75% 百分位）、中位数和中位绝对差（MAD），其中 IQR、中位数和 MAD 的单位为 meV/atom。仅比较具有相同 ICSD ID 的结构。此外，作者移除了所有含 F 或 O 的过渡金属化合物，因为这些化合物在 MP 中会获得 Hubbard U 校正，这与 MC3D 不可比，尤其是在纯 DFT 情况下。

图 2. 对基于 PBE、PBEsol 及底层实验参考结构 EXP 的若干方法，其形成能相对于实验的差异进行比较。用于计算形成能的不同方法 “calc” 包括：“Pure DFT” 计算（左列）、在 DFT 弛豫结构上评估的 MLIP 预测形成能 “PET-OMATPES r2 SCAN (unrelaxed)”（中列），以及使用 PET-OMATPES r2 SCAN MLIP 的完全 MLIP 弛豫结构及其相应 MLIP 形成能 “PET-OMATPES r2 SCAN (sym. relaxed)”（右列）。（上排）每个结构的形成能差异 $\Delta H_f^{calc}-\Delta H_f^{expt}$ 的直方图，分别在/从 PBE 弛豫结构（蓝色）、PBEsol 弛豫结构（橙色）和实验源结构 EXP（绿色）出发。EXP 仅用于 PET-OMATPES 弛豫，以研究 MLIP 弛豫在多大程度上复现从 DFT 弛豫结构出发时的结果。（中排）计算形成能 $\Delta H_f^{calc}$ 与同一相对于实验的差异之间的散点图，每个点代表一个结构。（下排）相对于实验的差异 $\Delta H_f^{calc}-\Delta H_f^{expt}$ 的汇总误差指标：均方根误差（RMSE）、平均绝对误差（MAE）和平均误差（ME），分别针对 PBE、PBEsol 和 EXP 给出。

图 3. 不同模型架构和特征组合的性能比较。a 预测形成能的平均绝对误差。b 稳定性翻转率，定义为 ML 预测与参考（PBEsol 或 PET-OMATPES r2 SCAN）之间稳定性分类不同的结构比例，其中能量高于凸包小于 25 meV/atom 的材料被视为稳定。结果针对两组特征（Magpie 和来自 PET-OMATPES 的潜特征 LFs）、PBEsol 和 r2 SCAN 两个目标，以及四类模型给出：Random Forest、Gaussian Process Regression（GPR），以及使用 RBF（KRR-RBF）和 Laplacian（KRR-LAP）核的 Kernel Ridge Regression。误差棒表示 30 个不同训练-测试划分的标准差。紫色点线和灰色虚线分别对应测试集中 PBEsol 和 PET-OMATPES r2 SCAN 相对于实验的基线 MAE。黑色点线表示实验不确定性。

图 4. 正则化对形成能 MAE 和稳定性翻转率的影响。两个面板均基于 PET-OMATPES r2 SCAN 数据。a KRR 模型随正则化强度变化时，在形成能预测精度与稳定性可靠性之间的权衡。每个点对应一个特定正则化参数 α，虚线连接同一模型-特征组合在递增 α 值 α ∈ {0.001, 0.01, 0.1, 0.4, 0.7, 1.0, 10} 下的点（通常从左到右）。带黑色边缘突出显示的数据点是在图 3 中展示的点。横轴显示稳定性翻转率（校正后稳定性分类发生变化的结构比例），纵轴显示 30 个训练-测试划分的平均测试 MAE（误差棒：标准差）。结果针对四种模型-特征组合给出：使用 Laplacian 和 RBF 核的 KRR，分别搭配 Magpie 或 LF 特征。b 对于使用 LF 特征、以不同正则化参数 α ∈ {0.001, 0.01, 0.1, 0.4, 0.7, 1.0, 10} 训练的 KRR-LAP 模型，稳定性翻转率随稳定性阈值变化的关系。阴影带表示 30 个训练-测试划分的方差。此外，插图显示从校正分布中随机采样时预期的翻转率。虚线竖线标记了面板 a 和图 3b 中使用的 25 meV/atom 阈值。

图 5. 零样本和 ML 校正 PET-OMATPES 形成能引起的稳定性分类翻转比较。热图显示相对于 PBEsol 基线，零样本 PET-OMATPES r2 SCAN 形成能以及进一步加入 ML 校正后的形成能所导致的稳定性分类变化。颜色标尺表示两种方法与实验一致性的平均差异，该差异也由每个单元格中的 Δ 值表示。正值表示与零样本 PET-OMATPES r2 SCAN 相比，ML 校正形成能相对于实验具有更好一致性，即 $|\delta\Delta H_f^{ML}|$ 小于 $|\delta\Delta H_f^{MLIP}|$。每一类别中的结构比例 $p$ 也被标出。数据汇总自全文分析的 30 个测试集。

图 6. 本文提出的 ML 方法与成熟 FERE 方法的比较。对于不同校正方法 “corr”：FERE-part、FERE-all 和 ML（KRR-LAP-LF，本文方法），给出每个化合物相对于实验的绝对偏差变化 $|\delta\Delta H_f^{corr}|-| \delta\Delta H_f^{pure\ DFT}|$。负值（绿色背景）表示相对于纯 DFT 值有所改善，正值（红色背景）表示变差。箱线图显示中位数（竖线）、IQR（箱体）和 1.5×IQR 须；单个数据点以垂直抖动叠加显示。
