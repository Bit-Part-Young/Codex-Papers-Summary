# 文献总结 - 快速准确的等变机器学习原子间势基础模型 - 2026

## 文献基本信息

- 英文原文标题：Fast and Accurate Foundation Models for Equivariant Machine-Learned Interatomic Potentials
- 中文标题翻译：快速准确的等变机器学习原子间势基础模型
- DOI 链接：论文原文未给出正式期刊 DOI；当前版本为 arXiv 预印本，arXiv:2607.28461v1，链接：https://arxiv.org/abs/2607.28461
- 作者：Sean R. Kavanagh, Chuin Wei Tan, Menghang Wang, Marc L. Descoteaux, Gabriel de Miranda Nascimento, Ulrik Unneberg, Laura Zichi, Francesco Libbi, Norma Rivano, Austin Glover, Vivek Bharadwaj, Anders Johansson, William C. Witt, Albert Musaelian, Boris Kozinsky
- 期刊名称：arXiv 预印本，physics.comp-ph
- 投稿 - 返修 - 接收 - 在线发表日期：论文 PDF 未列出期刊投稿、返修和接收日期；arXiv v1 在线发表日期为 2026 年 7 月 30 日。
- 数据/代码链接：
  - NequIP 模型、配置和包文件：https://nequip.net
  - 数据与分析代码：论文中标注为 doi.org/zenodo-to-publish-upon-acceptance
  - NequIP 代码：https://github.com/mir-group/nequip
  - Allegro 代码：https://github.com/mir-group/allegro
  - OpenEquivariance 代码：https://github.com/PASSIONLab/OpenEquivariance
  - cuEquivariance 代码：https://github.com/NVIDIA/cuEquivariance

## 文献总结

### 研究背景与核心问题

机器学习原子间势（MLIPs）已经成为计算材料科学和化学中的关键工具。随着 MPtrj、Alexandria、OMat24、MatPES、MAD 和 OMol25 等大规模第一性原理数据集出现，能够覆盖宽化学空间的“通用势”逐渐被当作基础模型使用：研究者先在大数据集上预训练，再在目标化学空间的小数据集上微调，以降低专用模型的数据生成成本。

论文关注的核心矛盾是：许多实际科学模拟，特别是分子动力学，需要同时具备高精度、高训练速度和高推理速度。等变 MLIP 通过在模型结构中直接编码旋转、反演和平移等物理对称性，通常可提高精度、数据效率和泛化能力，但在大规模基础模型训练与分子动力学推理中也面临计算成本问题。

本文的目标是在超大数据集条件下检验等变 MLIP 的速度-精度极限，并提出一组基于 NequIP 和 Allegro 架构的基础势模型。这些模型分别在 DIRECT、MPtrj、MPA 和 OAM 等无机材料数据集上训练，并在材料发现、热导率、近平衡热力学和力学性质等社区基准上验证。

### 模型与训练数据

论文训练了两类等变图神经网络模型。NequIP 使用原子中心消息传递架构；Allegro 建立在等变架构之上，但采用严格局域的、以原子对/边为中心的表示，不使用原子中心消息传递，因此适合高度可扩展的大体系并行推理。

训练数据包括 4 个规模和结构多样性逐渐增加的数据集：

1. DIRECT：约 18.6 万个结构，由 Materials Project 几何弛豫数据经降维编码聚类和分层采样得到。
2. MPtrj：约 158 万个结构，来自 Materials Project 中几何弛豫和静态计算轨迹。
3. MPA：约 1050 万个结构，由 MPtrj 与 Alexandria 平衡/近平衡结构组合而成，并去除与 Matbench Discovery 测试集重叠的结构原型。
4. OAM：约 1.13 亿个结构，由 OMat24 非平衡结构与 MPA 组合而成；训练时先用 OMat24，再在 MPA 上微调，以保持与 Materials Project 计算设置兼容。

模型命名采用 `{architecture}-{dataset}-{model size}`。其中 architecture 为 NequIP 或 Allegro，dataset 为 DIRECT、MP、MPA 或 OAM，model size 为 S、M、L 或 XL。

### 训练加速

论文指出，NequIP 基础设施中的图编译、分布式数据并行训练、优化张量积核、混合精度训练和加速核显著降低了大模型训练成本。图 1 显示，对于大 NequIP 和 Allegro 模型，这些优化提供 5-10 倍累积训练加速。

混合精度训练中，节点嵌入使用 float64，张量积使用 float32，读出再转回 float64；中间计算可使用 bfloat16 自动混合精度。作者发现混合精度对精度影响很小，并可使 NequIP 和 Allegro 分别获得最高约 1.35 倍和 3 倍训练加速。对于数值幅度较大的数据集，作者建议大部分 epoch 使用混合精度，最后用全精度短程继续训练，以保持精度。

结合分布式训练后，作者报告在 NVIDIA H100/H200 GPU 上，训练 1 亿级结构数据集的高精度基础势模型成本可降至约 100-750 GPU 小时。这使得高精度基础 MLIP 的训练从大型团队专属任务转变为单个研究组可承担的任务。

### 基准性能

论文在 Matbench Discovery、热导率基准和 MatCalc 基准上评估模型。NequIP-OAM-XL 在表 2 所列各项基准中均取得最佳精度：凸包能量平均绝对误差为 19.7 meV/atom，几何 RMSD 为 0.060 A，热导率 κSRME 为 0.129，定容热容误差为 4 J mol^-1 K^-1，预测力与 DFT 力幅值比为 98%。

随着模型尺寸和训练数据规模增加，材料发现和热导率性能总体改善。图 2 和图 3 显示，模型尺寸和训练数据规模与误差之间大体呈幂律关系。不过 NequIP-OAM-XL 在模型尺寸学习曲线中偏离简单幂律，说明在该尺寸附近精度开始饱和。

对于热导率，误差随数据规模增加更理想地持续下降。这说明非平衡构型对学习势能曲面梯度和二阶/三阶力常数非常重要。OAM 中来自 OMat24 的非平衡结构显著改善了热导率相关性能。

### 材料发现误差来源

材料发现基准中，从 MPA 扩展到 OAM 后，凸包能量误差改善并不显著。作者通过元素分解误差解释这一现象。图 4 显示，第一行多价过渡金属 V、Cr、Mn 和 Fe 的元素相关误差明显高于总体平均；Np 和 Pu 也表现为高误差离群点。

论文将这些误差归因于两个因素。第一，过渡金属化合物势能曲面本身复杂，局域轨道和方向性多体相互作用要求更高的径向和角向分辨率。第二，训练数据中 Hubbard U 修正在氧化物/氟化物与金属或非氧/氟化物之间选择性施加，会产生不一致的能量曲面目标。作者指出，排除第一行过渡金属后，材料发现凸包能量 MAE 从 19.7 meV/atom 降至 16.3 meV/atom；进一步排除 Np 和 Pu 后降至 13.9 meV/atom。

因此，作者认为后续改进材料发现 MLIP 的关键不只是扩大模型和数据规模，而是提高数据的化学与结构多样性，统一或多保真地处理过渡金属 d/f 电子体系，并发展能随局域化学复杂性自适应改变分辨率的模型架构。

### 热导率与声子相关性能

热导率基准检验势能曲面的平滑性和梯度精度。NequIP 模型在 κSRME 上通常优于 Allegro，且学习率随模型和数据规模增加更快。作者指出，Allegro 的力验证误差并不明显差于 NequIP，但 κSRME 更高，可能与严格局域架构的有效感受野限制，或边中心表示与原子中心表示在高阶力常数导数平滑性上的差异有关。论文未给出最终原因，而是将其作为未来工作问题。

### 速度-精度权衡与大规模可扩展性

论文将 matbench-discovery Combined Performance Score（CPS）与单 GPU 分子动力学推理速度比较，发现 NequIP 模型在多种体系尺寸下形成速度-精度 Pareto 前沿。NequIP-OAM-XL 与 eSEN-30M-OAM 具有相同 CPS，但推理速度约快一个数量级；中等和小型 NequIP 模型进一步提供显著速度提升，并保持与领先模型竞争的精度。

在多 GPU LAMMPS 分子动力学中，Kokkos 加速的 ML-IAP 接口和 OpenEquivariance 核支持 NequIP 消息传递模型高效并行。强标度和弱标度测试显示，NequIP-OAM-L 和 NequIP-OAM-S 在 4-256 个 GPU 上均有良好扩展。作者展示了使用 NequIP-OAM-S 在相对适中的节点数上进行约 1 亿原子模拟的能力。

### 主要意义

本文的贡献在于证明等变基础 MLIP 可以同时实现高精度、快速训练、高推理速度和良好并行扩展。对于需要大尺度分子动力学、热输运预测、材料发现和后续微调的研究者，本文提供了一组可用的 NequIP/Allegro 预训练模型和训练策略。

论文也强调，未来进步需要转向数据和架构的精细改进：增加化学/结构多样性，避免不一致 DFT 校正带来的系统误差，改进过渡金属和强关联体系描述，并发展可根据局域环境复杂性自适应分配模型容量的等变架构。

## 摘要翻译

机器学习原子间势（MLIPs）已经成为计算材料科学和化学的一种变革性工具；在大而多样的数据集上训练得到的通用势，如今已常规地作为“基础模型”部署，用于在目标化学空间中的下游微调。所得模型的许多科学应用，例如分子动力学（MD），既需要高推理速度和训练速度，也需要高精度。在这项工作中，我们考察等变 MLIPs 的极限；这类模型在模型架构中直接编码物理对称性，以实现这些相互竞争的目标，特别是在极大数据集、数据效率不再那么关键的情形下。我们展示了如何处理这种权衡，并给出一族 NequIP 和 Allegro 等变 MLIP 架构中的基础势。这些势在一系列社区基准上实现了领先的推理速度和强可扩展性，同时也具有优异精度；这些基准涵盖材料发现、热导率预测，以及近平衡力学和热力学性质。NequIP 基础设施中实现的加速现已允许在超大数据集上训练高精度基础势，并显著降低计算成本。同时，我们表明，提高材料发现模型精度的工作应集中于数据集多样性，以及对过渡金属化合物势能曲面进行改进且一致的描述。

## 引言翻译

机器学习原子间势（MLIPs）已经成为计算材料科学和化学不可或缺的工具 [1-3]。最近，大而多样的第一性原理模拟数据集，主要是密度泛函理论（DFT）数据集，如 MPtrj [4]、Alexandria [5]、OMat24 [6]、MatPES [7]、MAD [8] 和 OMol25 [9]，已经使 MLIPs 的训练成为可能。这些 MLIPs 能够在很宽的化学空间中以合理精度预测能量和力，通常被称为“通用势”。在大数据集上训练的势越来越多地被作为“基础模型”使用；它们提供一组预训练权重和参数，随后可在目标化学空间内的小数据集上重新训练或微调 [10-12]。已有研究表明，微调可显著降低下游应用所需的额外训练数据集尺寸，同时得到与专门构建的模型相当的预测精度 [10,12,13]。虽然这种方法减少了生成训练数据的时间，但所得微调模型的尺寸和推理速度可能成为科学模拟工作流中的限制因素。此外，在大规模数据集上训练大型通用模型仍然是一项困难且计算昂贵的任务，往往需要数周时间，因此阻碍了架构和超参数探索。

为解决这些未解决的问题，在这项工作中，我们提出一族来自 NequIP [14] 和 Allegro [15] 模型框架的等变图神经网络基础模型，这些模型在 MPtrj [4]、Alexandria [5] 和 OMat24 [6] 数据集上训练。NequIP [14] 框架率先发展了基于等变图神经网络（GNNs）的原子间势，其中旋转、反演和平移等物理对称性被直接纳入模型架构。已有研究表明，等变模型可提高 MLIPs 的精度、数据效率和泛化能力 [16-18]；若干最先进 GNN 模型也基于 NequIP 架构 [19-21]。Allegro [15] 在等变架构基础上采用严格局域表示，不使用原子中心消息传递，从而在大体系上实现高度可扩展的并行推理 [22]。值得注意的是，Allegro 使用原子对作为中心模型特征（图的边），并使用等变表示的迭代张量积来描述多体相互作用，而不是像 NequIP 那样以原子为中心。

这项工作得益于 NequIP 框架近期的基础设施发展 [23]，包括训练时图编译、用于可扩展多 GPU 训练的分布式数据并行（DDP）策略，以及优化张量积核 [24,25]。这些发展允许在大数据集上高效且可扩展地训练。我们使用多种社区基准验证这些模型的精度，包括几何弛豫和材料发现 [26]、非平衡声子相关性质预测 [7] 以及热导率 [27]，并展示出优异性能。我们发现，当前无机材料发现基准的精度主要受训练数据集中成分多样性，以及过渡金属化合物势能曲面描述的限制。最后，我们展示所训练模型的领先推理速度和优异可扩展性。

## 方法翻译

论文的明确方法部分为第 VII 节 “METHODS”。以下按原文顺序翻译。

所有模型的完整训练超参数和包文件均可通过 https://nequip.net 获得，也可在 https://doi.org/final-zenodo 获得；它们可被方便地下载，并与 NequIP 和 Allegro 一起用于微调应用。本文不同模型尺寸所改变的关键超参数见表 1。在所有情况下，特征向量不可约表示（irreps）的宇称被限制为球谐函数的宇称，即 $l=0,2...$ 时为偶，$l=1,3...$ 时为奇；对应设置为 `parity: false`。作者发现这可带来约 1.5-2 倍速度提升，而对精度影响较小（小于 3%）。作者指出，该选择仍然对应于 SO(3) 等变网络架构。本文使用 PyTorch 2.7.1、NequIP 0.16、Allegro 0.7、e3nn 0.5.6、OpenEquivariance 0.4 和 cuEquivariance 0.6；不过，用于微调的打包模型与这些软件的最新版本完全兼容。

如前文所述，作者发现推理时使用降低的浮点精度，例如 TensorFloat32，会在预测中引入显著噪声，尤其是在力预测中最明显。对于材料发现基准，这增加了几何弛豫所需的离子步数，而最终能量基本不受影响。对于热导率基准，力中的噪声会显著增加预测误差，如文献 [30,41] 所讨论。增大声子计算中的原子位移距离可部分降低低精度对基准精度的影响 [30,41]。如预期，从完整单精度 float32 增加到双精度 float64 推理并未进一步提高预测精度 [41,60]。

为支持在 TB 级大数据集上的高效训练，并同时使用分布式数据并行（多 GPU），作者采用 Lightning Memory Mapped Database（LMDB）格式 [61]，该格式已在 NequIP 架构中实现 [23]。作者指出，NequIP 模型的总参数数量对节点（原子）嵌入特征数 `type_embed_num_features` 相当敏感，但对速度和精度影响相对较小。这再次说明，模型参数量只能非常粗略地估计训练和推理速度的数量级。

作者尝试了自适应损失权重，其中损失系数根据验证误差更新在训练过程中动态更新，但对于这些大数据集，测试精度没有显著改善。这包括对 Ocampo 等人 [62] 所提方法的扩展；该方法趋向于 1:1:1 的能量:力:应力损失系数比。作者进一步让更新按初始损失系数加权，但仍未带来有意义的改善。不过，当合适的损失系数先验选择未知时，该方法可能更有益。

除图 1 所示结果外，作者还给出了使用 DIRECT [34] 数据集评估的训练速度，见图 S1，其趋势相同。所有训练速度测量中，NequIP 使用每 GPU 40 帧的 batch size，总 batch size 为 160，并采用表 1 中的 “large” 模型配置。对于 Allegro，为避免基线模型显存溢出，作者使用每 GPU 6 帧的较小 batch size，总 batch size 为 24，$l_\text{max}=2$，径向截断为 5 A，层数为 4。作者指出，来自图编译、加速张量积核和混合精度的具体加速因子取决于模型超参数；这些超参数影响矩阵乘法、张量积等不同数值操作所占的时间比例。由于自动混合精度在 PyTorch ≤ 2.7.1 中与 OpenEquivariance [24] 不兼容，作者未记录 NequIP 使用自动混合精度的训练速度结果，但预计最新 PyTorch 版本会支持。

近期研究 [63] 发现，大型 DFT 数据集的某些子集中存在非零净力，包括 OMat24 [6]；这表明电子密度和力可能未完全收敛。作者尝试仅使用净力（漂移）小于合力幅值 5% 或 10% 的帧训练，以此作为潜在相对误差度量。这会移除 OMat24 从头算 MD 子数据集中的几个百分点结构，但作者发现其对模型精度影响可以忽略，与其他观察一致 [6]。值得注意的是，这些构型中的总能量受欠收敛影响相对较小 [64]。作者也尝试只在 OMat24 的从头算 MD 子数据集上训练，因为文献 [41] 发现这样可改善同核双原子能量曲线；但作者同样发现，除材料发现精度略有下降外，该操作基本没有影响，而在完整 OMat24 [6] 数据集上训练的 NequIP 模型也表现出良好的同核能量精度 [51]。

对于 MatCalc [7] 几何弛豫基准，初始结构扰动使用相同随机种子（=8）为所有模型重新运行，以保证同类比较。凸包能量平均绝对误差（$E_\text{WBM,MAE}$）在 WBM 测试集中唯一结构原型集合上计算；该集合约包含 21.5 万个结构，来自约 25 万个化合物 [26]。为了将 $E_\text{WBM,MAE}$ 分解为图 4 中每个元素的值，作者使用按原子分数加权的绝对误差均值：

$$
\mathrm{MAE}_X=\frac{\sum_i f_{X,i}\left|E^{\mathrm{NequIP}}_{f,i}-E^{\mathrm{DFT}}_{f,i}\right|}{\sum_i f_{X,i}},
$$

其中 $f_{X,i}=N_{X,i}/N_{\mathrm{atoms},i}$ 为结构 $i$ 中元素 $X$ 的原子分数，求和覆盖完整 WBM [37] 测试集。Xe 在图 4 的逐元素误差分布中被省略，因为它在约 25 万个化合物的 WBM [37] 测试集中只出现一次（XeF2），因此不具有统计显著性。

模型训练主要在 Harvard University 的 FASRC Cannon 集群以及 NERSC Perlmutter 系统上，使用 NVIDIA A100/H100/H200 GPU 完成。总 batch size 为 640 帧，分布在 4-16 个 GPU 上。总模型训练成本从约 100 到 750 个 H200 GPU 小时不等。所有情况下均使用 AdamW 优化器，并使用 ReduceLROnPlateau 学习率调度。能量:力:应力（E:F:S）损失函数系数初始设置为 1:5:0.1；训练持续到力验证误差平台期，随后进行第二阶段训练，其中 E:F:S 权重为 1:1:0.1，初始学习率降低 10 倍，不使用混合精度，并采用随机权重平均 [33]，尽管后者影响可以忽略。能量损失使用逐原子能量，而不是总能量。对于 NequIP/Allegro-OAM-{model size} 模型，先在 OMat24 [6] 上训练，使用初始学习率 0.005 和权重衰减 1e-8；随后在 MPA 数据集上进行第二阶段微调。在 MPA 上训练时，初始学习率和权重衰减分别为 0.005 和 1e-8；在 MPtrj/DIRECT 数据集上训练时分别为 0.02 和 1e-3。在 OAM 和 MPA 上训练时使用梯度范数裁剪到 1；在 MPtrj 和 DIRECT 上训练时使用 0.01。Huber 损失函数的 delta 值为：能量 0.01 eV/atom，力 0.01 eV/A，应力 0.1 eV/A^3。作者也测试了力的分层 Huber 损失，对极端力幅值（>100 eV/A）使用逐渐减小的 Huber delta 值。该方法先前被发现有助于 MPtrj [4] 数据集训练稳定性 [65]，但在本文设置中影响可以忽略。孤立原子能量被用作模型训练中的参考原子能量位移，取自文中列出的公共仓库；MPtrj [4] 上逐元素均方根力幅值的平方根被用于初始模型能量尺度。

评估 matbench-discovery [26] 材料发现精度时，几何弛豫使用 FIRE [66] 优化器，最大离子力收敛阈值为 0.015 eV/A，最大弛豫步数为 200。计算 κSRME [27] 精度时，有限差分声子计算使用 0.035 A 位移距离。

Frontier 和 Perlmutter 上的 LAMMPS 标度测试使用 2026 年 3 月 30 日特性发布版 LAMMPS。初始硅结构来自 Materials Project [35]。在 NERSC Perlmutter 上，所有模拟运行于 80 GB HBM2e 显存的 NVIDIA A100 GPU。软件环境包括 Python 3.11.0、PyTorch 2.9.0+cu129、NequIP 0.17.1、NequIP-Allegro 0.8.2、e3nn 0.6.0 和 OpenEquivariance 0.6.6，以及 CUDA Toolkit 12.9。Cray 环境模块 `craype-accel-nvidia80` 和 `cray-mpich/9.0.1` 用于启用 GPU 加速和 MPI 通信。在 OLCF Frontier 上，模拟使用 AMD MI250X GPU；其 128 GB HBM2e 显存在两个 GCD 之间分配。软件环境包括 Python 3.11.15、PyTorch 2.11.0+ROCm7.2、NequIP 0.16.1、NequIP-Allegro 0.8.0、e3nn 0.5.9 和 OpenEquivariance 0.6.6。关键系统模块包括 `rocm/7.2.0`、`PrgEng-amd/8.6.0` 和 `cray-mpich/9.1.0`。

ASE [48] 和 LAMMPS [49] 分子动力学推理速度测试均使用与 LAMMPS 标度测试相同的金刚石结构硅体系，但采用较小超胞。这些单 GPU 速度比较在一块 NVIDIA A100-SXM4（80 GB）GPU 上进行，并使用每个模型公开记录的设置和可用加速器。评估 ASE 和 LAMMPS MD 运行时间时，模拟在 NVE 系综下进行，时间步长为 1 fs；先运行 1000 个不计时 warm-up 步，再运行 5000 个计时步。对于计算成本高得多的 PET-OAM-XL [8,67] LAMMPS 模型，使用 200 个 warm-up 步和 500 个计时步。除图 S9 中一部分 PET-OAM-XL LAMMPS 基准外，所有情况下均禁用降低精度的 TensorFloat32 算术，这与本文其他推理设置一致。虽然作者记录了 PET-OAM-XL 的守恒和非守恒变体推理速度，但图 5 中与其他守恒基础 MLIP 的比较只使用守恒模型速度。对于支持多个 LAMMPS 接口的 NequIP、Allegro 和 SevenNet，图 5 使用给定模型和超胞尺寸下任一接口记录到的最快推理速度；完整推理速度见图 S9。

对于 ASE 评估，NequIP 和 Allegro 使用 PyTorch 2.10.0 通过 `nequip-compile` 进行 ahead-of-time（AOTInductor）编译，并使用加速张量积核；NequIP 使用 OpenEquivariance [24] 核，Allegro 使用 cuEquivariance [25] 核。MACE-MPA-0 [65] 也使用 cuEquivariance [25] 张量积核；SevenNet-Omni [68] 由 FlashTP 核加速；Nequix MP PFT [69] 使用配置了 OpenEquivariance 核的 JAX 后端执行。ORB v3 [41] 使用 `model.compile()` 加速。eSEN-30M-OAM [30] 和 EquiformerV3 [70] 通过 FairChem/OCP calculator 路径评估，PET-OAM-XL [8,67] 通过 UPETCalculator 评估，GRACE [18,71] 模型使用带 TensorFlow GPU 支持的 TensorPotential calculator 评估。

为实现直接比较，同时适配各模型族互不兼容的软件依赖，作者准备了 4 个独立 LAMMPS 构建及匹配的 Python 环境；每个 LAMMPS 可执行文件均使用 GCC 12.2 和 CUDA 12.9.1 编译，所有运行均使用单 MPI rank。NequIP 和 Allegro 模型使用同一个 LAMMPS 构建（release patch 30Mar2026），包含 Kokkos [52] 和 ML-IAP 包，并链接 PyTorch 2.9.1（CUDA 12.6）、NequIP 0.17.1 和 Allegro 0.8.2。每个模型通过两种接口基准测试：（i）原生 pair styles，经 `nequip-compile` 导出为 AOTInductor 编译产物；（ii）Kokkos 加速的 ML-IAP 接口 [52]，其中 NequIP 集成 OpenEquivariance [24] 加速张量积核，Allegro 集成 cuEquivariance [25]。NequIP pair style 没有 Kokkos 实现，因此在单 GPU 上不使用 Kokkos 运行；其唯一 Kokkos 加速路径是 ML-IAP。Allegro pair style 和两个 ML-IAP 路径都使用 Kokkos GPU 后端。

对于比较模型，作者使用同一 LAMMPS/ML-IAP 构建运行 MACE-MPA-0 [65]，并将其用 `mace_create_lammps_model` 导出为 ML-IAP unified format。GRACE [18,71] 和 SevenNet [68] 使用专门的 LAMMPS 构建，以反映其不同接口。GRACE-1L 和 GRACE-2L 的小、中、大变体通过 TensorFlow 后端 pair style `grace` 评估；GPU 执行由 TensorFlow 运行时而非 Kokkos 管理。SevenNet-Omni 及其更大的 i12 变体通过两个接口评估：一个是使用 cuEquivariance 核的 ML-IAP 接口，另一个是基于 TorchScript 的 pair style `e3gnn`，在带 SevenNet 接口补丁和 FlashTP 张量积核的专用 LAMMPS 构建中运行。

最后，PET-OAM-XL [8,67] 通过 `metatensor/lammps` 的 `metatomic` 分支专用 LAMMPS 构建评估；该分支提供带 Kokkos GPU 后端的 pair style `metatomic` 接口。公开 v1.0.0 检查点使用 metatrain 的 `mtt export` 导出为 metatomic TorchScript 模型。该构建链接 PyTorch 2.10.0（CUDA 12.8）、metatomic-torch 0.1.11、metatensor-torch 0.8.5 和 metatrain 2026.2.1。作者测试 4 种配置：默认能量守恒模型，即通过预测势能自动微分得到力；以及非守恒变体 [67]，即由专用输出头直接生成逐原子力；每种都分别在禁用和启用降低精度 TensorFloat32 张量核心算术的情况下评估。该构建未配置 MPI，所有运行均使用单 Kokkos GPU rank。所有比较模型检查点均来自其各自公开发布版本。

除模型配置和包文件外，作为本文工作一部分生成的全部数据和分析代码，包括与其他模型架构的推理速度基准，均提供在 doi.org/zenodo-to-publish-upon-acceptance。

## 结论翻译

我们已经提出一族 NequIP [14] 和 Allegro [15] 架构中的等变基础势，覆盖一系列模型尺寸，并在规模和多样性不断增加的无机材料数据集上训练，这些数据集包括 DIRECT [34]、MPtrj [4]、MPA [5] 和 OAM [6]。这些模型在一系列成熟社区基准上实现了有竞争力的精度，包括材料发现 [26]、热导率 [27] 和近平衡性质 [7]，同时主导速度-精度 Pareto 前沿。第 S6 节所示的化学类型嵌入降维分析表明，基本化学关系是在没有显式编程的情况下学习得到的，并且在更大的模型尺寸下呈现出逐渐更清晰的化学结构。大规模基础势已经在支持多样而复杂的机器学习工作流。这个在广泛使用的 NequIP [14] 和 Allegro [15] 架构中构建的快速、准确预训练模型库，将为模型微调提供有用起点，并极大帮助原子建模社区研究者提高数据效率和精度。

这些结果得益于 NequIP 框架 [23] 近期的架构和基础设施发展，包括训练时图编译、加速张量积核 [24,25]、审慎的混合精度训练，以及分布式数据并行策略。合在一起，这些进展带来 5-10 倍累积训练时间加速，并将训练高精度基础势的成本降至数百 GPU 小时，现已达到单个研究组可承担的范围。结合近期在 LAMMPS [49] 中实现的 Kokkos 加速 ML-IAP 接口 [52]，这种接口为消息传递模型提供高效多 GPU 推理，这些进展打开了在相对适中的节点数上常规模拟约 1 亿原子体系的大门。此外，更新后的 NequIP 框架优先考虑可扩展性，使方法扩展、新型架构 [55-59] 或训练策略能够方便地构建在该核心框架之上，以避免重复工作，并充分利用这一加速、模块化且原生并行的基础设施。

我们的误差分布分析表明，MLIPs 在材料发现中的进一步进步，将不那么依赖原始模型或数据集缩放，而更依赖改进的数据：超越离子替换的更广化学和结构多样性，对 d/f 电子体系的一致处理，或有原则的多保真处理；以及改进的架构，包括自旋态，并考虑强关联体系对更高径向和角向分辨率的需求。在架构方面，能够随局域化学环境平滑改变径向和角向分辨率的模型，可以帮助调和不同元素/化合物复杂性之间的巨大差异，而不必统一膨胀模型容量。

## 结果/讨论章节子标题翻译

- I. 引言
- II. 训练加速
- III. 大模型训练
- IV. 基准性能
- IV.A 材料发现基准性能
- IV.B 热导率基准性能
- IV.C MatCalc 基准
- IV.D 精度-速度权衡
- V. 标度
- VI. 结论
- VII. 方法
- VIII. 致谢
- S1. 额外训练时间基准
- S2. 额外学习曲线分析
- S3. 其他社区模型的逐元素材料发现误差
- S4. 热导率和声子基准误差分析
- S6. 学习到的类型嵌入分析

## 图题和表题翻译

图 1. 加速模型训练。使用 MPtrj 数据集训练大 NequIP 和 Allegro 模型的训练速度，表示为每 GPU 小时训练的数据帧数（带能量和力的原子结构）。训练速度在无/有图编译（`torch.compile`）、使用标准张量积核或近期实现的 OpenEquivariance（用于 NequIP）和 cuEquivariance（用于 Allegro）核、以及无/有混合浮点精度策略（TensorFloat32 或自动混合精度）的情况下测量。训练时间在 NERSC Perlmutter 系统上使用单节点 4 块 NVIDIA A100 40 GB GPU 记录，更多细节见第 VII 节。为标准化比较使用相同 batch size；但作者指出，混合精度和加速核也会显著降低 GPU 显存需求，允许更大 batch size，从而带来二阶训练时间加速。

图 2. 模型尺寸学习曲线。在 OAM 数据集上训练的 NequIP 和 Allegro 模型（NequIP/Allegro-OAM-{model size}）在 Matbench Discovery 基准套件上的测试误差随模型尺寸的变化。包括未见化合物凸包能量预测的平均绝对误差（$E_\text{WBM,MAE}$，左）和 103 个二元化合物热导率的无量纲对称相对平均误差（κSRME，右）。虚线表示对数据的最小二乘幂律拟合（$L=a\cdot x^{-\alpha}$），图例给出拟合缩放指数 α 和决定系数 $R^2$。表 2 给出数值。模型超参数、训练数据集和命名语法见第 III 节。

表 1. 本文训练的 NequIP 和 Allegro MLIPs 的关键模型超参数。$l_\text{max}$ 指神经网络模型特征的最大旋转阶数。MLP = 多层感知机。

表 2. 在 MP 和 OAM 数据集上训练的 NequIP 和 Allegro 模型性能指标，精度基准来自 Matbench Discovery 和 MatCalc 测试套件。包括未见化合物凸包能量预测平均绝对误差（MAE，$E_\text{WBM,MAE}$）、未见化合物预测几何的均方根偏差（RMSD）、103 个二元化合物热导率的无量纲对称相对平均误差（κSRME）、定容热容 MAE（$C_{v,\text{MAE}}$）以及预测力幅值与参考力幅值的平均比值（$f/f_\text{DFT}$）。模型超参数、训练数据集和命名语法见第 III 节，基准评估参数的额外细节见第 VII 节。NequIP-OAM-XL 模型在每个基准上均给出最佳精度。

图 3. 训练数据学习曲线。本文训练的最大 NequIP 和 Allegro 模型（NequIP-{dataset}-XL 和 Allegro-{dataset}-L）在 Matbench Discovery 基准套件上的测试误差随训练数据集尺寸变化。包括未见化合物凸包能量预测的 MAE（$E_\text{WBM,MAE}$，左）和 103 个二元化合物热导率的无量纲对称相对平均误差（κSRME，右）。虚线表示对数据的最小二乘幂律拟合（$L=a\cdot x^{-\alpha}$），图例给出拟合缩放指数 α 和决定系数 $R^2$。表 2 给出数值。模型超参数、训练数据集和命名语法见第 III 节。

图 4. 材料发现的逐元素误差。使用 NequIP-OAM-XL 模型，在 matbench-discovery 材料发现基准中，凸包能量平均绝对误差（MAE）在元素周期表上的逐元素分布。误差以 meV/atom 显示，并使用对数色标。最大逐元素误差出现在含多价第一行过渡金属（V、Cr、Mn、Fe）的化合物、低出现率锕系元素（Np、Pu），以及 Eu、Ta、Te、Pb 和 H。

表 3. MatCalc 基准结果；包括几何弛豫后与 DFT 参考的结构相似性（$d_\text{MAE}$，无量纲）、每原子形成能（$E^f_\text{MAE}$）、体模量（$K_\text{MAE}$）、剪切模量（$G_\text{MAE}$）、定容热容（$C_{v,\text{MAE}}$）和非平衡力幅值（$f/f_\text{DFT}$，无量纲）。OAM 指先在 OMat24 数据集上进行初始模型训练，再在子采样 Alexandria 和 MPtrj 数据集上微调的流程。MatterSim 数据集包含 Alexandria、MPtrj 和闭源合成数据。UMA 数据集包含 OC20++、OMat24、OMol25、ODAC25 和 OMC25 数据集。

图 5. 精度-速度权衡。matbench-discovery 的 Combined Performance Score（CPS）相对于分子动力学（MD）推理速度作图；体系为 64 到 13,824 个原子的金刚石 Si，使用单块 NVIDIA A100-SXM4（80 GB）GPU。MD 模拟分别使用 Atomic Simulation Environment（ASE，空心标记）和 LAMMPS（实心标记）；LAMMPS 仅用于具有 LAMMPS 接口的模型，并使用每个模型公开文档中的设置和可用加速器。每个面板中，精度与推理速度的 Pareto 前沿分别以虚线和实线黑线表示 ASE 和 LAMMPS。在当前版本中，CPS 以 5:4:1 的相对权重平均 matbench-discovery 基准中的材料发现、热导率和结构相似性精度。较大体系尺寸中缺失的模型因显存不足错误而崩溃。

图 6. NequIP 的多 GPU 标度。大、小 NequIP 模型（NequIP-OAM-L 和 NequIP-OAM-S）在 LAMMPS 中使用带 OpenEquivariance 核和 `torch.compile` 的 ML-IAP 接口时的强标度（上）和弱标度（下）性能。MD 模拟使用 32.8k 到 102.5M 原子的金刚石结构硅体系，在 Perlmutter 和 Frontier 集群上分别使用 NVIDIA A100（80 GB）和 AMD MI250X GPU。每个 Perlmutter 节点包含 4 块 GPU，每个 Frontier 节点包含 8 个 MI250X GCD。

## 补充图题翻译

图 S1. 加速模型训练（使用 DIRECT 数据集）。使用 DIRECT 数据集训练大 NequIP 和 Allegro 模型的训练速度，表示为每 GPU 小时训练的数据帧数。训练速度在无/有图编译、使用标准张量积核或 OpenEquivariance/CuEquivariance 加速核、以及有/无混合浮点精度策略的情况下测量。训练时间在 NERSC Perlmutter 系统上使用单节点 4 块 NVIDIA A100 40 GB GPU 记录。相同 batch size 用于标准化比较；混合精度和加速核也显著降低 GPU 显存需求，允许更大 batch size 并带来额外训练加速。

图 S2. 模型尺寸学习曲线 - 小到大模型拟合。OAM 数据集上训练的 NequIP 和 Allegro 模型在 Matbench Discovery 基准套件上的测试误差随模型尺寸变化；包括凸包能量预测 MAE 和热导率 κSRME。虚线表示排除 NequIP-OAM-XL 后的最小二乘幂律拟合，并给出 α 和 $R^2$。

图 S3. 训练数据学习曲线 - DIRECT 到 MPA 拟合。本文最大 NequIP 和 Allegro 模型在 Matbench Discovery 基准套件上的测试误差随训练数据集尺寸（DIRECT、MP、MPA、OAM）变化；包括凸包能量 MAE 和热导率 κSRME。虚线表示排除 OAM 数据集后的最小二乘幂律拟合。

图 S4. 使用 eSEN-30M-OAM 的材料发现逐元素误差。使用 eSEN-30M-OAM 模型，在 matbench-discovery 材料发现基准中，凸包能量 MAE 在元素周期表上的逐元素分布。最大逐元素误差出现在多价第一行过渡金属（V、Cr、Mn、Fe）、低出现率锕系元素（Np、Pu），以及 Eu、Ta、Te、Pb 和 H；这与 NequIP-OAM 模型一致。

图 S5. 使用 MACE-MPA-0 的材料发现逐元素误差。使用 MACE-MPA-0 模型，在 matbench-discovery 材料发现基准中，凸包能量 MAE 在元素周期表上的逐元素分布。最大逐元素误差出现在多价第一行过渡金属（V、Cr、Mn、Fe）、低出现率锕系元素（Np、Pu），以及 Eu、Ta、Te、Pb 和 H；这与 NequIP-OAM 模型一致。此处 Al 的相对误差明显高于 NequIP-OAM 或 eSEN-30M-OAM。

图 S6. 分解的热导率基准误差。NequIP/Allegro-OAM 模型在原始 κSRME 基准测试集 103 个二元化合物上的平均模分解热导率误差（左）和声子频率误差（右）随声子频率变化。热导率主要由低频模式主导，因此 κMode 误差绘制在 0-15 THz 的低能范围内，并由总热导率 κTotal 归一化。κMode 和声子频率误差图分别采用宽度为 0.2 和 0.5 THz 的高斯平滑。

图 S7. Materials Project 结构上的平均声子频率误差。NequIP-OAM、Allegro-OAM 和 Allegro-MP-L 模型在所有 26,234 个具有 DFT 参考声子数据的 Materials Project 结构上评估得到的声子频率平均绝对误差 $|\Delta\omega|$，随声子频率变化。

图 S8. Materials Project 结构上的平均声子频率误差（平滑）。与图 S7 相同，但使用高斯平滑以显示趋势。

图 S9. LAMMPS 单 GPU 推理速度。本文训练的 NequIP-OAM 和 Allegro-OAM 模型，以及其他社区基础势（GRACE-1L/GRACE-2L、MACE-MPA-0、SevenNet-Omni 和 PET-OAM-XL）的 LAMMPS 分子动力学推理速度（每秒时间步数）随体系尺寸变化。每个面板对应固定原子数（64 到 13,824），使用金刚石硅超胞。NequIP 和 Allegro 模型分别通过原生 pair style 和 Kokkos 加速 ML-IAP 接口显示。PET-OAM-XL 通过 Kokkos 加速 metatomic 接口运行，包含能量守恒模型和非守恒直接力模型，每种均评估有/无 TF32 张量核心算术。所有模拟在单块 NVIDIA A100（80 GB）GPU 上运行。

图 S10. NequIP-OAM 模型中化学类型嵌入的主成分分析（PCA）降维。NequIP-OAM 模型（S、M、L、XL）学习到的化学类型嵌入向量沿前 2 个主成分投影。散点按周期族、周期、元素周期表区块和 Pauling 电负性着色。

图 S11. NequIP-OAM 模型中化学类型嵌入的 PCA 降维 - 带标签。NequIP-OAM 模型学习到的化学类型嵌入向量沿前 2 个主成分投影，并以元素身份标注。散点按元素周期表区块着色。

图 S12. NequIP-OAM 模型中化学类型嵌入的 UMAP 降维。NequIP-OAM 模型学习到的化学类型嵌入向量的 UMAP 2D 投影图。散点按周期族、周期、元素周期表区块和 Pauling 电负性着色。

图 S13. NequIP-OAM 模型中化学类型嵌入的 UMAP 降维 - 带标签。NequIP-OAM 模型学习到的化学类型嵌入向量的 UMAP 2D 投影图，并以元素身份标注。散点按元素周期表区块着色。

图 S14. NequIP-OAM 模型中化学类型嵌入的 t-SNE 降维。NequIP-OAM 模型学习到的化学类型嵌入向量的 t-SNE 2D 投影图。散点按周期族、周期、元素周期表区块和 Pauling 电负性着色。

图 S15. NequIP-OAM 模型中化学类型嵌入的 t-SNE 降维 - 带标签。NequIP-OAM 模型学习到的化学类型嵌入向量的 t-SNE 2D 投影图，并以元素身份标注。散点按元素周期表区块着色。
