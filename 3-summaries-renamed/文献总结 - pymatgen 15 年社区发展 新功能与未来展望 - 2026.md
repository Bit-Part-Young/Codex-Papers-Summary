# 文献总结 - pymatgen：十五年社区发展、新功能与未来展望 - 2026

---

## 文献基本信息

- **英文标题**：pymatgen: 15 years of community growth, new functionality, and future prospects
- **DOI**：原文未提供。
- **作者**：Janine George、Matthew K. Horton、Aaron D. Kaplan、Seán R. Kavanagh、Janosh Riebesell、Andrew S. Rosen、Haoyu Yang 等共 166 位作者；完整名单见下文“作者全名单”。
- **作者单位**：原文以 a–eh 标注众多单位，跨大学、国家实验室和企业；以下列出主要作者所对应的单位，完整单位列表见原文第 1–3 页。
    - a Materials Chemistry, Federal Institute for Materials Research and Testing (BAM), Berlin, Germany。
    - b Institute of Condensed Matter Theory and Optics, Friedrich Schiller University Jena, Jena, Germany。
    - c Isotropy, LLC, Seattle, United States。
    - d Materials Sciences Division, Lawrence Berkeley National Laboratory, Berkeley, United States。
    - e Yusuf Hamied Department of Chemistry, University of Cambridge, Cambridge, United Kingdom。
    - f Cavendish Laboratory, University of Cambridge, Cambridge, United Kingdom。
    - g Department of Chemical and Biological Engineering, Princeton University, Princeton, United States。
    - h Institut für Physik, Humboldt-Universität zu Berlin, Berlin, Germany。
    - x Department of Materials Science and Engineering, University of California, Berkeley, United States。
    - cq Aiiso Yufeng Li Family Department of Chemical and Nano Engineering, University of California San Diego, La Jolla, United States。
    - eg Energy Storage and Distributed Resources Division, Lawrence Berkeley National Laboratory, Berkeley, United States。
    - eh Department of Materials Science and Engineering, National University of Singapore, Singapore。
- **期刊**：原文未提供；该文件为 arXiv 预印本（arXiv:2610.23538v1）。
- **日期**：投稿、返修、接收、在线发表日期原文未提供；arXiv 版本日期 2026-10-16。
- **数据与代码链接**：https://github.com/janosh/pymatgen-2-paper；pymatgen 项目代码库为 https://github.com/materialsproject/pymatgen。

**作者全名单**：Janine George; Matthew K. Horton; Aaron D. Kaplan; Seán R. Kavanagh; Janosh Riebesell; Andrew S. Rosen; Haoyu Yang; Felix Adams; Mahdi Amachraa; Oxana Andriuc; Omar A. Ashour; Saurabh Bajaj; Ella Banyas; Luis Barroso-Luque; Karlo Berket; Noam Bernstein; Arpit Bhardwaj; Ali Hussain Umar Bhatti; Samuel M. Blau; Brandon Bocklund; Alexander Bonkowski; Danny Broberg; Guillaume Brunin; Kyle Bystrom; Charles A. Cardot; Rees Chang; Chi Chen; Xin Chen; Wei Chen; Yuan Chiang; Kamal Choudhary; Orion A. Cohen; Miguel D. Costa; Stephen T. Dacek III; Maarten De Jong; Tom Demeyere; Alan K. Dozier; Alexander Dunn; Shyam Dwaraknath; Maxwell T. Dylla; Kristjan Eimre; Alexander R. Epstein; Christina Ertural; Marco Esters; Matthew L. Evans; Johannes Falke; Adam Fekete; Bernard Field; Alexandr Fonari; Nathan C. Frey; Dale W. Gaines II; Alex M. Ganose; Matteo Giantomassi; Rhys E. A. Goodall; Petre-Flaviu Gostin; Aayush Gupta; Viet-Anh Ha; Geoffroy Hautier; Niclas Heinsdorf; Michael F. Herbst; Tingzheng Hou; Patrick Huck; Yuji Ikeda; Adam J. Jackson; Saivenkataraman Jayaraman; Finn R. Kearns; Sunghyun Kim; Ryan S. Kingsbury; Adam M. Krajewski; Yu Kumagai; Matthew C. Kuner; William T. Laderer; Xiang-Guo Li; Weitang Li; Yu Hsuan Liang; Hanyu Liu; Ke Liu; Miao Liu; Ahmad Lutfi; Olivier Marchand; Matthew J. McDermott; Bharat K. Medasani; Fanchen Meng; Kyle D. Miller; Henrique Miranda; Rohith Srinivaas Mohanakrishnan; Joseph H. Montoya; Guy C. Moore; Benjamin J. Morgan; Jason M. Munro; Koki Muraoka; Aakash A. Naik; Willis O’Leary; Anthony Onwuli; Jaesuk Park; Drew F. Parsons; Kai Pei; Guido Petretto; Thomas A. R. Purcell; Ji Qi; Xiaohui Qu; Ihor Radchenko; Nav Nidhi Rajput; Francesco Ricci; Benjamin S. Rich; William D. Richards; Gian-Marco Rignanese; Xiaoxu Ruan; Germain Salvato Vallverdu; Jonathan Schmidt; Jimmy-Xuan Shen; Ryuichi Shimogawa; Kohei Shinohara; Arunima K. Singh; Eric Sivonxay; Stef Smeets; Tess E. Smidt; Andrei Sobolev; Evan Walter Clark Spotte-Smith; Christopher Stihl; Wenhao Sun; Jack D. Sundberg; Yuta Suzuki; Leopold Talirz; Hanmei Tang; Eric Taw; Cooper Tezak; Félix Therrien; Scott D. Thiel; Steven B. Torrisi; Mark E. Turiansky; Katharina Ueltzen; Michiel J. van Setten; Josua Vieten; Sudarshan Vijay; Nicholas Wagner; Frank Wan; Zhenbin Wang; Jingyang Wang; Amanda Wang; Logan Ward; Thomas Warford; David Waroquiers; Mingjian Wen; Oskar Weser; Nicholas Winner; Donald Winston; Michael Wolloch; Brandon M. Wood; Rachel Woods-Robinson; Yihan Xiao; Yaoshu Xie; Firat Yalcin; Ruo Xi Yang; Weike Ye; Pezhman Zarabadi-Poor; Jinzhe Zeng; Hongsheng Zhao; Kaifeng Zheng; Zhuoying Zhu; He Zhu; Nils E. R. Zimmermann; Daniel Zügner; Kristin A. Persson; Anubhav Jain; Shyue Ping Ong。

---

## 论文内容详细总结

### 研究背景与目的

这是一篇回顾与展望性质的论文，而非报告单一材料体系实验的常规研究。pymatgen 于 2011 年为 Materials Project 的高通量密度泛函理论（DFT）工作流而创建，最初提供晶体学操作、对称性分析、VASP 输入输出、电子结构和相图工具。作者回顾其 15 年发展，讨论软件设计、跨代码互操作、社区影响、维护难题和未来方向，并提炼社区驱动型科研软件的经验。

---

### 核心设计与科学工作流

- pymatgen 通过可复用的材料对象、模块化分析功能和基于 Monty 的 JSON 序列化，为结构操作、配位环境、电子结构、相图、声子及多种计算软件的输入输出提供共同基础。它使计算产物能够与数据库、工作流和其他程序衔接。
- 接口覆盖 VASP、Quantum ESPRESSO、FHI-aims、CP2K、ABINIT、Q-Chem、phonopy、LOBSTER 等。与 ASE 的功能重合但重点不同：前者偏重复杂材料数据分析，后者的 calculator 与动力学接口偏重原子模拟；Structure 与 Atoms 可转换，支持组合使用。
- 作者以声子计算为例，列出从数据库获取结构、约化原胞、生成电子结构计算输入、弛豫、生成位移超胞、计算力、由 phonopy 求力常数直至绘制声子谱的八步流程，说明 pymatgen 的“连接器”作用。

---

### 社区规模、案例与新功能

- 原始论文截至 2026 年 9 月被引用超过 4000 次，2025 年单年接近 1000 次；2018 年 8 月至 2025 年 12 月 PyPI 下载约 2320 万次，2026 年每月超过 50 万次。作者指出自动化 CI 下载会抬高这一指标。图 2 给出 276 位曾提交 PR 的贡献者、626 个依赖包、2713 个依赖仓库以及超过 65 万名 Materials Project 注册用户等生态指标。
- 上游依赖有 NumPy、SciPy、pandas、Matplotlib、Plotly、spglib、NetworkX、monty 等；下游有 atomate、quacc、doped、ShakeNBreak、matminer、MatGL、PyXtal、LobsterPy 和 AMSET 等。作者将影响概括为加速专项工具开发、规范共用分析流程、提高可重复性、提供教学入口以及推动开放科学。
- 缺陷建模案例展示了超胞与点群分析、结构搜索、计算输入输出、元数据和溯源的复用；doped、pydefect、PyCDT、pymatgen-analysis-defects 等在此基础上构建。数据驱动案例强调数据库与 CIF 解析、氧化态及局域配位描述符、matminer 特征生成和可解释的化学启发式方法。
- 新功能涉及离子扩散分析、基于 MatGL 的 MLIPs 结构弛豫、无序材料有序构型估计、ChemEnv/CrystalNN 局域环境分析、LOBSTER 键合分析，以及独立安装的 io 与 analysis 命名空间扩展。

---

### 挑战、解决思路与展望

- 维护主要依靠科研人员志愿贡献与 Materials Project 的机构支持。核心维护任务仍集中于少数人，稳定经费、明确的贡献路径和认可维护劳动是持续发展的条件。
- 历史技术债包括文件解析语法不一致、JSON 表示低效、复杂继承层级等。采用 YYYY.MM.DD 日历版本号时，用户须查阅发布说明判断升级影响；弃用功能目前通过 FutureWarning 和通常 6–12 个月的移除窗口通知下游。
- 2025 年 7 月 31 日测试报告覆盖 60,242 / 76,389 条可执行 Python 语句，整体为 78.9%；core 为 90.2%，entries 为 85.8%，io 为 83.6%，vis 为 13.9%。测试套件即使并行运行仍超过半小时。作者主张静态检查、针对性测试与人工审查的 AI 辅助共同保障质量。
- 近十年活跃贡献者通常每年约 30–75 人，2019 年最高；近五年略有下降。治理、贡献模板、及时代码审查、论坛支持与学术导师传承，是吸纳新维护者的主要途径。
- 未来重点包括更广泛的软件接口、社区审查的文档、PyTorch/JAX 与结构图表示、可视化、编译扩展带来的性能改进、领域扩展包、GPU 张量后端，以及通过 MCP 等接口向 AI 代理暴露经过验证的材料分析工具。作者强调这些属于社区机会与发展方向，而非已实现功能。

---

## 章节翻译

### 摘要

我们回顾 Python Materials Genomics（pymatgen）软件库的发展，反思 15 年的社区成长和已经建立的最佳实践。当前版本的 pymatgen 建立在稳健的开源基础之上，强调其协作性质。在过去十年里，pymatgen 已发展为材料科学领域规模最大的开源代码库之一。我们详细介绍 pymatgen 如何支持先进的计算材料科学工作流、如何适应不断变化的需求，以及从持续壮大的社区中获得的经验；这些经验也可为 pymatgen 开源社区之外提供指导。面对计算材料科学和材料信息学当前快速变化的格局，pymatgen 将继续演进。我们讨论管理 pymatgen 社区驱动式演进所面临的挑战和潜在解决方案，并展望其未来发展。

---

### 1 引言

Python Materials Genomics（pymatgen）[1] 于 2011 年推出，旨在为高通量密度泛函理论（DFT）工作流中的材料分析提供稳健、可复用的软件基础。先前基于 Java [2] 构建的基础设施已经显得陈旧。Python 的普及、函数式与面向对象设计的结合、快速开发周期以及互操作性，使其成为现代计算材料科学软件的理想平台。由这一实际需求产生的 pymatgen，经过 15 年的发展，已经成为该领域使用最广泛的开源软件库之一 [3]。今天，pymatgen 是 Materials Project [4, 5] 的基石，是数百个下游软件包的依赖，也是电池材料、缺陷建模、机器学习原子间势（MLIPs）和材料信息学 [6] 等研究领域的标准工具包（图 1 和图 2）。

pymatgen 的发展历程提供了反思的机会。科学软件很少能像图 1 所示那样获得广泛的跨学科采用，同时保持长期持续开发。pymatgen 在十多年间一直处于活跃开发状态，其最初的软件论文现在每年获得 1000 次引用。它催生了计算材料科学领域的工具生态系统 [5, 7, 8]。理解这一过程如何以及为何发生，其经验远超 pymatgen 本身。

在这篇回顾文章中，我们评述使 pymatgen 获得广泛采用的设计原则和互操作理念。我们追踪贡献者社区和下游软件包生态系统的增长，考察维护如此规模的基础设施所伴随的技术与组织挑战。最后，我们勾勒下一发展阶段最重要的方向。在全文中，我们力图提炼适用于构建并维持社区驱动型科学软件这一更广泛挑战的经验；随着计算方法在材料发现中越来越居于核心地位，这一挑战也越来越重要。

---

### 5 挑战与解决方案

在十多年间维护和发展 pymatgen 这样规模的项目，带来了独特的技术、组织与社区挑战，也为更广泛的科学软件社区提供了宝贵经验。我们的经历凸显了在可持续性、互操作性、治理、贡献者引导和社区增长之间取得平衡的重要性。下面讨论遇到的主要挑战及可能的应对方式。

#### 5.1 可持续性与维护者资源

成熟的开源科学软件面临的最关键挑战或许是长期可持续性。不同于拥有专职开发团队的商业软件，pymatgen 主要通过学术研究人员的志愿贡献发展；软件开发必须与研究论文、教学和其他职业压力竞争。这一模式虽培育了社区的主人翁意识，却在维护、代码审查能力和长期功能开发方面造成结构性张力。

Materials Project 提供了关键的机构支持，包括聘用专职开发和工程人员、提供计算资源及组织基础设施。通过提供基础设施和维护，pymatgen 成为容纳特定分析及应用领域材料科学代码的平台；若无此平台，这些代码可能永远不会公开或被复用。这种结合机构支持与社区贡献的混合模式，对 pymatgen 的长久发展至关重要。然而，软件维护的经费仍难获取，因为资助机构强烈偏好新研究而非基础设施维护。德国国家研究数据基础设施中的 FAIRmat [84] 以及 Molecular Sciences Software Institute（MolSSI）[85] 等项目，是把计算和数据基础设施视为值得持续投入的关键研究基础设施的重要进展。

pymatgen 培养了分布全球的贡献者群体（图 6），新贡献者也不断加入（图 5），使项目对单一机构资源变化具有一定韧性。不过，维护负担集中在少数核心开发者身上，仍是持续存在的担忧。我们希望清晰的贡献指南、及时的代码审查，以及通过署名机会、论文致谢和社区可见度明确认可贡献者，能够帮助维持参与度并扩大活跃维护者群体。

这种渐进式开发的观点与 Digital Discovery 最近提出的 Commit 文章概念 [86] 相契合；该概念使对既有软件、数据和硬件论文所作改进能够以可引用的形式发表。虽然本文是一篇完整的回顾文章，背后的动机相似：通过透明、社区驱动的迭代，激励并奖励可持续的科学软件开发。持续进步仍依赖稳定资助、明确的新成员引导路径，以及认可维护工作的激励机制。我们将在这一观点文章中概述若干策略。

#### 5.2 向后兼容与 API 演进

成熟软件库中的一项根本张力，是在 API 稳定性和改进需求之间取得平衡。pymatgen 的早期设计决策积累了技术债，例如从文件解析 Python 对象的语法不一致、Python 对象的 JSON 表示低效、复杂的面向对象继承，以及相似对象不断增多。pymatgen 开发者已认识到这些挑战，需要谨慎评估，以确保向后兼容，同时不阻碍进一步开发。由于 pymatgen 使用 YYYY.MM.DD 格式的日历版本号，用户目前需要查阅发布说明，以评估升级的影响。

面对数千名用户和数百个依赖包，pymatgen 在 API 稳定性方面肩负重大责任。破坏兼容性的变更可能在生态系统中连锁传播，扰乱研究工作流，并要求多个项目协调更新。为此，pymatgen 正采用成熟的弃用最佳实践：被弃用的功能会发出 FutureWarning，并给出清楚的移除时间表，通常为 6–12 个月，以便下游维护者调整。重大变更通过发布说明、GitHub 讨论和 matsci.org 论坛传达。命名空间包架构（pymatgen-io-*、pymatgen-analysis-*）进一步使专门 API 得以独立演进，减少破坏性变更对核心库的影响。

对于成熟的基础设施软件库，向后兼容是与社区达成的约定。以可预测的移除时间逐步弃用功能，对于像 pymatgen 这样拥有庞大用户群的代码库持续演进、同时尽量降低对下游研究的影响，至关重要。

#### 5.3 测试覆盖率与代码质量

如图 7 所示，2025 年 7 月 31 日的覆盖率报告记录，在 76,389 条可执行 Python 语句中，60,242 条受到测试覆盖（78.9%），但不同模块差异很大。core 的覆盖率为 90.2%，entries 为 85.8%，io 为 83.6%，而可视化模块 vis 仅为 13.9%。图中的单元面积和覆盖率百分比均来自该报告；软件包覆盖率按覆盖语句数和可执行语句数之和计算。这种不均衡反映了真实的权衡：有些模块需要 VASP、Gaussian 等须许可的外部可执行程序才能进行有意义的测试，有些涉及长时间运行的操作，而可视化代码需要渲染后端，使无界面的持续集成（CI）更复杂。测试资源因此有策略地集中在服务最多用户的核心模块。

通过 GitHub Actions 运行的 CI 一直是重要的质量控制机制。CI 的具体实现随时间变化，但通常包括在每个拉取请求中、针对多个 Python 版本运行 pytest 或类似测试套件。测试覆盖率也会被跟踪和报告。Python 生态系统的开发工具快速转向 Rust，使 pymatgen 的 CI 流水线和本地开发工作流显著加速。尤其是静态类型分析（如 mypy、Pyright）帮助在开发阶段捕获微妙错误，否则它们可能直到测试或生产使用时才显现。展望未来，基于 Rust 的类型检查器 ty 一旦发布稳定版，其速度将足以与 LLM 编码代理形成紧密反馈循环，在数秒而非数分钟内捕获类型错误；即使对 pymatgen 这样的大型代码库也是如此。如果实施，这将使开发者能够快速迭代至正确代码，而无须等待慢得多的测试套件完成。pre-commit 钩子会在本地执行这些检查。不过，单元测试仍然必要；尽管已经并行化，当前测试套件运行仍超过半小时，继续给贡献者造成阻力。提高测试效率仍是持续的优先事项。

前沿大语言模型（LLMs）的出现正显著减轻 pymatgen 的维护负担。在 LLM 辅助下，编写测试、添加类型注解、改进文档字符串和重构遗留代码等任务能够加速。对于 15 年积累的技术债，这尤其有价值。引入 CodeRabbit、Cursorbot 或 Claude Code 等 AI 驱动的代码审查工具，还可以对拉取请求提供自动初审，进一步减轻维护者工作量。早期在大型代码库中尝试基于 LLM 的代码审查时，受上下文窗口和模型能力所限，常产生噪声，例如过于冗长的审查；如今这些工具已经明显成熟，能够可靠处理复杂变更集，并发现本来需要缓慢而费力的人工检查才能发现的真实问题。LLMs 也帮助新来者了解陌生代码，降低贡献门槛。这些 AI 辅助工具已切实提高 pymatgen 小规模维护团队的处理能力。同时，审慎审查仍然关键：必须确保 AI 辅助的贡献符合社区对正确性、可维护性和科学可靠性的标准，并确保贡献者充分理解最终代码，能够承担长期维护责任。

大规模项目的质量最好通过多层保障获得，而非依靠单一指标。快速的静态类型和格式检查、针对具体问题的单元测试，以及经人工审查的 AI 辅助，相结合时比只关注其中一部分更能提高每单位维护时间所获得的可靠性。

#### 5.4 治理以及贡献者和用户引导

作为 Materials Project 分析工具的核心组成部分，pymatgen 的治理遵循 Materials Project 利益相关者确立的原则；这些原则又借鉴了 NumPy [55] 和 NumFOCUS 等成熟社区组织采用的最佳实践。负责采纳和执行行为准则的 MP 成员与软件利益相关者，合称 Materials Project Software Foundation（MPSF）。MPSF 致力于为 MP 软件生态系统建立民主治理结构，例如推动将 MP 软件纳入 NumFOCUS 基金会索引。

这些行为准则为新贡献者营造欢迎的环境，旨在培养更长期的社区参与，从而使 pymatgen 受益。随着 pymatgen 的范围继续超出小型核心维护团队的能力，对较小众功能集的社区维护变得势在必行。营造欢迎新贡献者的环境，对确保 pymatgen 长期可持续至关重要。过去十年中，活跃贡献者人数通常每年约为 30–75 人，2019 年人数最多（图 8）。过去五年活跃贡献者略有下降，使治理和引导策略更加重要。年度提交次数也呈类似情况，尽管不同提交的规模可能差异很大。

我们的经验表明，社区成功增长不仅依赖吸引贡献者，也依赖建立便于提交、审查、复现和维护贡献的流程。我们认为，pymatgen 的广泛采用不能仅归因于其技术能力。相对较低的贡献门槛和及时响应的代码审查文化，在扩大并维持贡献者社区方面发挥了重要作用。结构化的问题报告、贡献模板、自动化测试和分层代码审查，都帮助 pymatgen 超越少数维护者所能支持的规模。这些做法共同帮助社区开发的新功能有效并入项目，减少贡献者的阻力，鼓励长期参与。

随着更多资历较浅的社区维护者为 pymatgen 作出贡献，他们最终会受邀负责 pymatgen 的部分模块。有意维护核心功能集的初级维护者，将由更有经验的维护者委派处理日常维护。这既确保社区提交的问题及时得到处理，也使资深维护者能够处理软件方向、优化等更大议题。由于 pymatgen 的分析工具是 MP 工作流和数据流水线不可或缺的一部分，只要 MP 继续履行使命，这些功能事实上就有维护保障。不过，较边缘的 pymatgen 功能需要这种社区驱动的维护结构，以免无人维护并失去功能。

pymatgen 发展带来的一项重要经验是，健康的开源生态系统并不限于代码贡献者。matsci.org 等社区讨论论坛和支持渠道，在用户引导、传播最佳实践，以及发现未来贡献者和维护者方面发挥关键作用。这些资源帮助支持工作突破核心开发团队的能力上限，同时加强社区参与。

通过学术指导和研究网络传递专业知识同样重要。许多新贡献者和用户曾在已有 pymatgen 使用经验的研究组接受训练，因此知识、开发实践和社区规范能够传给学生、博士后研究人员及合作者。这些研究人员后来转到新机构并建立自己的研究组，便产生扩散效应，扩大采用范围，培养下一代贡献者和维护者。正式的社区支持结构与人与人之间的知识传承相结合，是维持 pymatgen 增长和影响力的关键因素。

#### 5.5 依赖项与依赖方

如前文所述，大量材料科学代码依赖 pymatgen（见图 3b），而 pymatgen 本身依赖科学计算、绘图和数据科学的开源生态系统（图 3a）。pymatgen 是计算材料科学基础设施底层的重要组成部分，处于基础软件包与数百个下游依赖方之间，因此其依赖管理影响整个生态系统。pymatgen 遵循 Scientific Python 社区的 SPEC 0 政策 [87]，规定最低版本限制，同时避免设置最高版本上限，以防下游软件包的依赖解析冲突。当上游库引入破坏性变更时——例如 NumPy 2.0 C API 迁移 [55]——pymatgen 必须迅速适应，而且往往要先于自身的依赖方，以免阻塞更广泛的生态系统。这种双向责任是维护社区基础设施的反复出现的主题：变更会沿依赖图向上、向下传播，任一方向的延迟适应都会在整个生态系统中累积影响。这表明，像 pymatgen 这样被广泛采用的软件，需要反应及时的维护团队，才能避免成为更广泛生态系统的瓶颈。

---

### 6 展望与未来发展

pymatgen 已从一款专门工具演变为计算材料科学的基石。它的增长体现了材料信息学社区的协作精神，以及开源软件在科学研究中的重要性。

虽然 pymatgen 的核心功能相对稳定，但较边缘的功能需要小型维护团队之外的社区持续审查。提高最关键 pymatgen 软件库的性能是其发展的关键。pymatgen 在 v2022.0.0（2021 年 3 月）引入了命名空间包，使 pymatgen“命名空间”内的“附加”包能够独立安装和维护，即可从 pymatgen.io 和 pymatgen.analysis 导入。关键的是，这将附加包的发布节奏与核心库分离；一个软件包在早期开发阶段通常需要更高的发布频率，不再受 pymatgen 本身更慢、更审慎的发布周期限制。独立的 pymatgen-core 包进一步支持了这一点；它现在是 pymatgen 的一个依赖项，提供基础材料科学数据结构及输入输出和分析功能，供其他开发者构建新功能。

以目前的范围而言，要扩展和完善 pymatgen 的功能集，拥有大型开发团队将有利于有效维护。随着 pymatgen 的范围和采用程度继续增长，我们将下一步发展视为高影响力的社区机会。具体而言，更广泛地共同承担维护任务——代码审查、问题分类以及小众子模块的错误修复——能够加强参与和长期维护。贡献者在这些角色中积累经验后，自然可以成长为副审查者和维护者。

材料科学中有许多活跃领域可受益于 pymatgen 关键功能集的扩展。这包括为流行的电子结构代码（如 Quantum ESPRESSO）、原子尺度代码（如 LAMMPS、GROMACS），以及连续体、相场和多物理场代码提供种类更丰富、控制更深入的 io 扩展。然而如前所述，任何未置于可独立安装命名空间中的功能扩展，都需要相应的社区审查。

虽然 https://matsci.org 等社区论坛和 pymatgen 问题跟踪器提供了重要支持，但文档的扩展仍大有空间，才能与软件库令人印象深刻的广度相称。一个有前景的方向是由社区审查、LLM 辅助的工作流，它可在不增加核心维护者负担的情况下提高文档覆盖范围。

由社区需求和材料科学新趋势所启发的高影响力开发机会包括：

**机器学习集成。** 随着 ML 方法越来越多地进入材料发现与设计 [6]，这一方向可能持续重要。高价值的贡献包括原生支持 PyTorch、JAX 等现代框架，为神经网络架构实现高效的结构到图转换，以及加强与 Matbench Discovery [48] 等基准测试框架的集成。

**可视化与用户体验。** 与 Crystal Toolkit [88]、pymatviz [46] 和 MatterViz [89] 更紧密的集成，可降低使用门槛。有益的社区工作包括增强 Jupyter notebook 支持、交互式结构操作，以及生成可直接用于发表的图件。

**性能优化。** 尤其通过有策略地使用编译扩展，仍存在重大改进机会。如今 pymatgen 的运行情形与创立之初不同：早期它用于组织速度慢得多的 DFT 计算，Python 及其高度面向对象的软件结构带来的额外开销可以忽略。然而，随着速度极快的 ML 力场模拟兴起，这种开销已变得显著，更深入的优化越来越有价值。moyo 项目 [90] 给出了成功案例：它把 spglib 的对称性分析工具迁移至 Rust，同时通过绑定保留易用的 Python API。类似方法可以加快结构匹配、近邻搜索、凸包计算等经常使用且计算密集的操作。

**扩展包生态系统。** 其增长将强化 pymatgen 的联邦式架构：稳定的核心，辅以由领域专家维护的专用命名空间包，例如 pymatgen-analysis-diffusion [41] 和 pymatgen-io-openmm。增加扩展包的数量和质量，既可分散维护负担，也能使专门领域快速迭代。多尺度建模以及原子尺度与介观尺度模拟的衔接等新功能领域，最适合开发为扩展包，而非扩大核心。

**GPU 兼容性。** 一个有前景的方向，是在大量使用数组的代码路径中更广泛地支持张量后端（如 PyTorch），从而实现 GPU 加速，并可能提高大规模分析的速度。

**代理式 AI 工具。** pymatgen 功能可通过工具接口（包括模型上下文协议 MCP 服务器）提供给基于 LLM 的代理。Monty 序列化可促进数据交换，而明确的工具实现、模式定义和输入验证则支持可靠的工具使用。这些工具可向代理工作流提供化学、材料科学和物理分析能力。

我们欢迎各层次的贡献，从错误报告、文档改进到新功能和扩展包。项目的 GitHub 仓库、文档网站和社区论坛为新贡献者提供了入口。

---

## 结果与讨论子标题翻译

- 2 概述与设计原则
    - 2.1 背景
    - 2.2 互操作性与比较性工具
- 3 社区采用与影响
    - 3.1 软件包生态系统
    - 3.2 案例研究
        - 3.2.1 缺陷建模工具
        - 3.2.2 数据驱动的启发式评估与机器学习
        - 3.2.3 可迁移性与经验教训
- 4 新功能

---

## 图表题翻译

图 1：引用最初 pymatgen 论文的工作中选取的研究主题；借助 LLM，将 OpenAlex 的主要主题归入五个主题分支。每个分支最多显示四个主题。节点颜色和色标使用相同的对数计数尺度；分支计数为所显示子节点之和，根节点颜色则固定，以便在视觉上加以区分。

图 2：pymatgen 生态系统中的不同影响层级。从中心向外依次为维护者、贡献者、下游软件包开发者、pymatgen 直接用户，以及通过 Materials Project 间接受益的用户。数据来源和采集日期见补充材料 S2 节。

图 3：pymatgen 子软件包与上游和下游的使用关系。（a）pymatgen 子软件包（中）对第三方 Python 软件包（左）的上游使用关系。（b）依赖软件包（右）对 pymatgen 子软件包（中）的下游使用关系。连线宽度表示在所分析源代码中静态检测到的 API 调用位置数。两幅图显示了选定的依赖项与下游仓库；仓库选择和筛选方法见补充材料 S3 节。这些子软件包大致对应 pymatgen 的三种常见用法：输入输出（io）、材料对象操作（core），以及分析或支持模拟的功能（analysis）。

图 4：pymatgen 仓库中的开发活动。（a）截至 2025 年 12 月 31 日合并的全部 2494 个非机器人拉取请求，按照有序关键词规则各分配一次；标题无法匹配的归入“其他／未分类”。这些主题是根据标题粗略划分的类别。（b）2012—2025 年各日历半年（1—6 月和 7—12 月）每个软件包的提交次数，以对数色标显示。

图 5：每年合并的非机器人 pymatgen 拉取请求，按合并时贡献者的任期分组；任期从作者首次提交 PR（包括未合并的提交）时算起。年份为合并日期；包括截至 2025 年 12 月 31 日合并的全部 2494 个 PR，与图 4a 一致。任期分组互不重叠，一年定义为 365.25 天。

图 6：按贡献者国家统计的 pymatgen 拉取请求地理分布。国家由 GitHub 个人资料和单位快照推断，并辅以人工整理的映射；这些信息不一定代表每次贡献发生时贡献者所在的位置。276 位贡献者中有 67 位无法确定国家，对应 2498 个已合并 PR 中的 136 个，因此未绘入地图。数据来源和采集日期见补充材料 S6 节。

图 7：2025 年 7 月 31 日 coverage.py 报告中的 pymatgen Python 代码结构和代码行覆盖率。单元面积表示可执行语句数，颜色表示被测试覆盖的比例。父级百分比根据所覆盖语句与可执行语句的汇总值计算。模块最多按三级路径组成分组；不足 1500 条语句的组并入“其他”单元，不足 5000 条语句的子软件包作为单个单元显示。

图 8：2012—2025 年 pymatgen 每年的活跃贡献者人数和非合并提交次数。

---

## 指定章节翻译

### 2 概述与设计原则

#### 2.1 背景

pymatgen 最初于 2011 年开发，目的是支持 Materials Project [1, 4, 5]。为此，pymatgen 提供了晶体学操作、对称性分析、与 Vienna Ab Initio Simulation Package（VASP）密度泛函理论（DFT）代码 [9] 的集成，以及基础电子结构和相图分析所需的工具。这些基础功能使研究人员能够将计算材料科学的许多环节自动化和标准化，为高通量材料发现奠定基础。

此后，pymatgen 显著扩展，纳入新功能，并适应不断变化的材料科学和材料信息学格局 [6]。影响其发展的主要趋势包括：

1. 研究数据管理日益重要 [10]；
2. 用于可重复模拟和实验的自动化工作流兴起 [10-12]；
3. 越来越多地使用机器学习预测材料性质 [6, 13]；
4. 计算资源更加充足，使更复杂的分析、机器学习任务和模拟成为可能。

如今，pymatgen 旨在通过为各个层次的研究人员提供综合工具包，加快材料发现 [14]。虽然晶体学操作和电子结构分析等初始目标仍居于核心地位，但为满足不断变化的社区需求，其能力已经大幅扩展。现在，pymatgen 提供晶体学与结构分析工具，包括配位环境分析、电子结构解析、热力学和相图构建、声子性质分析，以及与多种电子结构代码的接口。此外，它还提供用于材料性质预测中机器学习应用的可复用工具，作为材料信息学软件包的基础 [15]；这体现了它从材料分析库演变为更广泛的材料信息学平台。pymatgen 在模块化、可复用的软件框架中实现这些核心材料分析功能，使常见任务无须反复重新实现，让用户和下游开发者能够专注于特定领域的专门分析与应用。同样的模块化和可复用性，对 AI 驱动的工作流也可能越来越有价值：基于 LLM 的代理可将成熟的 pymatgen 功能作为科学推理与分析中值得信赖的构件。因此，pymatgen 致力于成为功能强大、灵活且可靠的软件工具 [16]，服务于日益复杂的计算材料科学和材料信息学研究工作流。

从 pymatgen 广泛的社区采用及代码库持续增长中得到的一条重要经验是，科学软件必须不断演进，以满足所属领域的新兴需求；缺乏这种适应能力，就有过时的风险。它还必须不断吸纳和支持新开发者；我们认为，缺少友好的环境，开源开发就无法持续。较低的贡献门槛和及时响应的维护工作支持了 pymatgen 的增长，促进社区参与，也使新功能能够及时整合。

#### 2.2 互操作性与比较性工具

pymatgen 的一项优势是互操作性：它能够读取多种分子和结构文件格式，并从数据库自动获取分子和结构。此外，pymatgen 还提供与多种电子结构／DFT 代码的接口，例如 VASP [9]、Quantum ESPRESSO [17]、FHI-aims [18]、CP2K [19]、ABINIT [20]、Q-Chem [21]，以及与 phonopy [22, 23] 或 LOBSTER [24] 等后处理工具的接口。

组织异构计算工作流时，一项关键挑战是对代码之间传递信息所使用的数据结构进行规范化。不同代码通常各有专门的输入输出数据结构，妨碍相关模拟工具之间的互操作。例如，几乎所有分子 DFT 代码都接受以 `.xyz` 文件表示的分子几何构型作为输入，但配置计算参数——自洽场收敛判据、力收敛判据、基组等——以及存储计算输出的具体格式，各代码并不相同。

通过规范化这些数据的表示方式，pymatgen 使构建复杂工作流时能够顺畅地串接不同模拟工具的输出。尤为重要的是，在运行复杂工作流时，工作流的来源记录、元数据和进度通常存储于外部数据库。pymatgen 在设计时就考虑了这些要求，因此支持符合 JSON 规范的对象序列化与反序列化，以便与能够存储 JSON 数据的数据库互操作。

pymatgen 也与其他材料科学工具互为补充，其中最突出的是 Atomic Simulation Environment（ASE）[25]。两个软件包都提供 DFT 和量子化学代码的解析器，也都提供操作结构和分子的工具，但侧重点不同。pymatgen 以复杂材料数据分析为中心 [26]，支持从氧化态预测到热导率建模的任务。ASE 则侧重原子尺度模拟，通过晶体和分子数据的规范化，提供与 pymatgen 中对应功能类似的基础能力。其 calculator 框架整合了量子化学互操作能力，以及内置的几何优化与分子动力学功能。

pymatgen 强调材料分析对象和基于 Monty 的序列化；ASE 则通过 calculator 和动力学接口专注于原子尺度模拟。两者均提供持久化机制，二者结构表示之间的转换使互补的工作流成为可能。

这种差异意味着，pymatgen 常与 ASE 联合用于组织工作流，因为某些功能，例如由原子间势驱动的分子动力学，只能在 ASE 中使用。为简化两个代码的联合使用，pymatgen 支持在表示材料的 pymatgen `Structure` 对象与 ASE `Atoms` 对象之间转换。在多样且快速演进的研究生态系统中，让单一代码主导社区采用既不现实，也不可取。重点应是代码之间的互操作性，使用户能够结合两个软件包各自的优势，而非追求排他性。因此，代码维护者有责任与其他开发者建立并维持良好关系，在工程约束允许的范围内尽可能使互操作顺畅。

这种高度互操作性，使计算材料分析能够顺畅融入多样的研究工作流。以一种常见的声子计算工作流为例，它可能包括：

1. 手动或使用 pymatgen API 工具，从 ICSD [27] 或 Materials Project [4, 5] 数据库获取晶体结构。
2. 使用 pymatgen 中基于 spglib [28, 29] 的对称性和结构变换工具，将结构约化为原胞。
3. 使用 pymatgen 将原胞写为所选量子化学代码要求的文件格式，并可选择编写其他计算输入文件。
4. 使用所选量子化学代码进行几何弛豫。
5. 将弛豫后的结构直接读入 pymatgen，并使用 `pymatgen.io.phonopy` 接口生成一组原子位移超胞。
6. 用所选量子化学代码计算每个位移超胞的力，同时固定已位移原子的位置。
7. 使用 phonopy [22, 23] 解析原子位移计算，并求得原子间力常数。
8. 使用 phonopy 或 `pymatgen.io.phonopy` 接口绘制声子色散；后者还支持声子能带结构和态密度分析。分析 Grüneisen 参数则还需要在多个体积下进行声子计算。

这是一个简单的例子，但有助于说明 pymatgen 综合材料分析功能和广泛互操作性的用途。如今，计算材料研究工作流已广泛将 pymatgen 同时用作核心分析工具包，以及连接量子化学代码和先进科研软件包的顺畅纽带。

尽管 pymatgen 支持与许多代码的接口，但应注意，这些接口在很大程度上由 Materials Project 所开展的研究方向驱动。因此，VASP 和 Q-Chem 接口开发得很充分，因为 Materials Project 经常使用它们。另一些与 PACKMOL [30]、ATAT [31] 或 Zeo++ [32] 的接口，则分别是为研究非晶态材料、构型无序晶体材料或材料孔隙率的工作流而开发。这些接口可能与 ASE 或 pyiron [33] 中的接口重叠，但更多情况下并不重叠。我们无意列出 pymatgen 原生对接的全部代码——这种列表必然很快过时——只按字母顺序列举自第一篇 pymatgen 论文发表以来新增或显著增强的几个接口 [1]：ABINIT [34]、CP2K [19]、icet [35]、JDFTx [36]、LAMMPS [37]、LOBSTER [24]、OpenFF [38]、phonopy [22, 23] 和 Q-Chem [39]。pymatgen 的可扩展性使其能够在需求出现时迅速开发新的代码接口。

---

### 3 社区采用与影响

pymatgen 的增长不仅体现在功能集上，也体现在不断扩大的用户群，以及材料科学多个子领域的社区参与上（图 1）。其应用跨越储能与能量转换、催化、缺陷、材料信息学，以及通过机器学习进行材料发现等不同领域 [26]。此外，pymatgen 的影响遍及材料信息学社区的多个层级：从维护者和贡献者，到下游软件包开发者、pymatgen 直接用户，以及通过 Materials Project 的功能间接受益的用户（图 2）。这种广泛影响与采用程度的持续增长相呼应。下载次数以及将 pymatgen 列为依赖项的软件包数量稳步增加，表明它在材料科学社区中得到广泛而持续增长的采用。自 2013 年论文发表以来，pymatgen 已被引用超过 4000 次 [1]，仅 2025 年就接近 1000 次（Google Scholar，访问于 2026 年 9 月）。2018 年 8 月至 2025 年 12 月，pymatgen 在 Python Package Index（PyPI）上的下载量约为 2320 万次；2026 年每月超过 50 万次。不过，我们指出，自动化持续集成（CI）测试可能抬高这些数字。

#### 3.1 软件包生态系统

除了上一节讨论的常见材料分析直接用途，许多针对计算材料科学不同研究领域的软件包也构建在 pymatgen 框架之上。值得注意的下游软件包——其中一些见图 3b——包括：

1. atomate [28]、custodian、quacc [40]：高通量计算材料科学工作流。
2. pymatgen-analysis-diffusion [41]：扩散分析工具套件。
3. doped [42]、ShakeNBreak [43]：缺陷建模与结构搜索，建立在 pymatgen-analysis-defects [44] 和 PyCDT [45] 的基础上。
4. pymatviz [46]、SMACT [47]、matminer [15]：材料信息学工具包。
5. matbench-discovery [48]、AIRS [49]、MatGL [50]、torch-sim [51]：用于材料科学的机器学习。
6. PyXtal [52]：在对称性约束下生成和操作原子结构。
7. LobsterPy [53]：自动分析 LOBSTER 输出，以获得概述性的键合信息。
8. AMSET [54]：电子输运性质建模。

如此多样的下游软件包体现了 pymatgen 的可扩展性，以及它在材料建模和材料信息学生态系统中的基础作用 [6]。当然，pymatgen 本身也建立在基础性的开源 Python 软件包之上，如用于数值运算的 NumPy [55]、SciPy [56] 和 pandas [57, 58]，用于绘图的 Matplotlib [59] 和 Plotly [60]，用于对称性分析的 spglib [28, 29]，用于图分析的 NetworkX [61]，以及用于序列化的 monty，如图 3 所示。

总体而言，pymatgen 对材料科学社区的影响包括：

1. 加快各个领域的研究 [6]，包括促进专门的材料分析工具包快速发展（图 3b）。
2. 使核心材料分析程序标准化。
3. 通过易用的序列化和分析工具提高可重复性。
4. 为学生和职业生涯早期研究人员提供易于使用的教学工具 [1]，例如 https://github.com/materialsvirtuallab/matgenb 和 https://github.com/sp8rks/MaterialsInformatics。
5. 被工业研发工作流采用 [4, 5]。
6. 促进开放科学和协作开发 [16]。

#### 3.2 案例研究

如上所述，许多先进的材料分析软件包以 pymatgen 代码库为基础，支持复杂、专门的领域研究工作流。下面简要讨论两个案例，说明 pymatgen 框架如何促成先进且复杂的材料分析。

##### 3.2.1 缺陷建模工具

缺陷建模是一个快速发展的领域。一方面，计算能力和方法的进步使这些计算越来越可行；另一方面，缺陷物种对于晶体管、太阳能电池、透明导电材料、电池、量子比特等多种材料技术至关重要 [62]。缺陷模拟可能是一个漫长而复杂的过程，因为它需要许多不同任务 [42, 63, 64]：结构操作、对称性分析、电子结构代码的输入文件生成与输出解析、用于可重复性的轻量元数据与序列化，以及与 Materials Project 等数据库建立接口以进行相图分析。此外，许多任务针对缺陷这一特殊情形还有专门要求，包括生成高效且适当的超胞（以平衡计算成本与准确性）、确定缺陷点群对称性、构型简并度和位点重数（对于破坏对称性的超胞）、用于结构搜索的定向畸变、针对大型复杂结构分析的高效算法、子相图的智能算法等 [65]。

现在已有多个开源工具包利用 pymatgen 的核心功能实现缺陷建模工作流的各个阶段，包括 doped [42]（图 3b）、pydefect [63]、PyCDT [45]、pymatgen-analysis-defects [44]、ShakeNBreak [43]、AiiDA-defects [66] 和 pydecs [67]。这些工具包在缺陷建模社区得到广泛使用，有助于加快这一技术关键领域的研究，同时减少人为错误，并降低新研究人员的入门门槛。pymatgen 广泛的功能以及灵活的模块化结构，是这些下游工具得以发展的重要基础，使其功能能够针对特定用途加以定制。

这些发展尤为令人期待的一点是，它们大幅减轻了缺陷模拟中数据共享与可重复性的负担；由于涉及步骤繁多，这本是一项特别困难的任务 [65]。通过 pymatgen 提供的面向对象架构，以及它和其依赖项 monty 提供的高效 JSON 序列化与反序列化工具，汇集并导出完整元数据和计算来源记录所需的人工工作显著减少。这些发展有助于建立清晰的社区可重复性标准和预期，提高缺陷建模研究的质量，同时为该领域未来的数据库和机器学习工作提供可靠基础 [65]。

##### 3.2.2 数据驱动的启发式评估与机器学习

pymatgen 是一个强大的工具包，使材料科学中的大规模数据分析与机器学习研究成为可能。这些能力对于揭示特定材料性质的新设计原则，以及开发基于特征的机器学习模型至关重要；后者常是材料加速平台（MAPs）和自主实验室的核心组成部分 [11, 12]。

通过 pymatgen 与材料数据库的直接接口——Materials Project API（现已拆分为独立软件包）或 OPTIMADE API [68]——研究人员能够方便地获取包括机器学习目标值在内的大型数据集。这些数据集是从数据出发评估设计原则和启发式规则，以及开发机器学习模型的基础。使用 Cambridge Structural Database [69]、Inorganic Crystal Structure Database [27] 或 MAGNDATA [70] 等其他晶体结构来源时，pymatgen 能够把（磁性）晶体学信息文件（CIFs）直接解析为原子尺度模拟所需的输入对象，便于建立大型结构化数据集。根据需要，pymatgen 支持按成分或晶体对称性简便地筛选。此外，pymatgen 提供许多后处理功能，使目标值更易生成。

化学启发式规则常用于启发设计原则或机器学习模型的特征。这些特征十分有价值，因为它们提供可从物理和化学角度解释的描述符：既能提高模型的可解释性，也能用作对机器学习输出的科学一致性检验。许多此类描述符和设计原则——例如与稳定性、可合成性、缺陷能量学和磁性有关的描述符与原则——依赖于对氧化态和配位环境的准确判定，而 pymatgen 均可进行评估。pymatgen 实现了多种氧化态判定的启发式方法，例如基于键价和或根据成分作简单推测；也实现了多种配位环境判定方法，例如基于最短距离或 Hoppe 有效配位数的方法，以及 `local_env` 和 `chemenv` 模块中更先进的方法 [71, 72]。此外，pymatgen 与 matminer [15] 深度集成。matminer 简化了机器学习工作流中常用特征的生成，进一步支持启发式规则的推导和验证。在这里，pymatgen 格式直接用作生成机器学习特征的输入。

总之，pymatgen 提供了处理材料数据、提取特征和发展启发式规则的框架，使其成为现代数据驱动型材料信息学的重要工具。通过将化学、晶体学和物理知识编入可复用的数据结构、描述符及分析工作流，pymatgen 将专家领域知识转变为可扩展的材料发现资源。

##### 3.2.3 可迁移性与经验教训

还有许多其他案例表明 pymatgen 影响了材料建模的多个子领域，包括低维材料、表面切割与分析、高通量材料发现和自动化工作流，以及磁结构枚举等。

建立在 pymatgen 之上的细分领域建模软件包获得成功，表明只要为结构操作、氧化态估计、DFT 代码输入输出等常见任务提供稳健功能，领域专家就能方便地将其扩展至更专门的研究工作流。pymatgen 将这些核心材料分析功能实现在可供下游软件包方便导入的模块化代码结构中，省去了重复实现常见任务的需要，使研究人员可以专注于特定领域的专门分析，例如预测缺陷浓度。这样一来，某些功能实际上成为该领域特定任务的社区参照，例如 `StructureMatcher`；随着软件广泛使用，其方法选择和默认参数也得到普遍采用。pymatgen 之类的软件包由于被广泛使用并受到专家监督，能够成为社区的重要参考，帮助推广一致的实践和方法。因此，一种自然的标准化得以形成：被广泛采用的实现塑造了计算材料分析中的共同做法。

这些先进模拟工作流成功的另一个重要方面，是在 pymatgen 核心模块中通过巧妙的算法、向量化、Cython 代码或其他方法实现较高计算效率。这保证了下游用途的效率和可扩展性，使基于 pymatgen 的复杂工作流成为可能，例如在巨大的材料搜索空间中进行高通量筛选，或分析低对称性的大型缺陷超胞结构。同时，性能优化必须与代码可读性、可维护性和易理解性取得平衡，因为后者对于鼓励社区贡献和确保项目长期持续至关重要。

最后，清楚地传达代码弃用和破坏兼容性的变更，对于依赖 pymatgen 的众多下游科学软件包顺利、不间断地开发和维护至关重要。

---

### 4 新功能

pymatgen 的增长紧跟材料科学研究的趋势，体现了它在推动科学进步中的关键作用。锂、钴替代电池电极的建模长期推动着 pymatgen 原子尺度分析工具的发展。pymatgen-analysis-diffusion 扩展包 [73] 源于一个较小的扩散率分析工具子模块，后来这些工具迁移至独立的命名空间包。它们能够根据分子动力学轨迹更快地估算离子迁移能力，也包含依据电子电荷密度寻找可能的拓扑保持型离子插入缺陷位点的工具 [74]；在根据势能面的过渡态式映射估算离子迁移能力时，会用到这些位点。

近来，机器学习（ML）方法 [6]，尤其是机器学习原子间势（MLIPs）[75]，已成为无需借助成本更高的电子结构方法、便能快速估计原子结构的实用手段。pymatgen 通过外部 Python 软件包 MatGL [50] 集成了其中一些结构预测工具。例如，用户可以使用 M3GNet [75]、CHGNet [76]、TensorNet [77] 和由 MatPES 导出的模型 [78] 等常见的图神经网络 MLIPs，快速弛豫晶体结构。还可以在 pymatgen 中直接使用 MLIPs，通过枚举可能的有序排布并选取预测能量最低的构型，估计无序材料的小晶胞有序表示。

分析局域配位环境对于理解原子结构与材料特性之间的联系也一直至关重要。这些认识有助于识别产生相似性能的结构基元，例如有利于离子迁移的框架。pymatgen 通过与 LOBSTER [24] 对接，支持分析电子电荷密度和电子键合。如下文进一步讨论的，pymatgen 可借助 ChemEnv [72] 和 CrystalNN [79] 等方法，以计算上可承受的代价分析局域原子配位环境。CrystalNN 还可用于生成与 MLIPs 特征向量相似的结构嵌入，进而快速估计结构相似性 [79]，并借助 robocrys 软件包 [80] 自动生成人类可读的材料描述。来自 ChemEnv 的局域配位环境分析、CrystalNN 相似性估计，以及基于 CrystalNN 生成的材料描述，如今都是 Materials Project 数据构建流水线的标准分析产物，并作为其核心数据的一部分分发。

其他可在 `io` 和 `analysis` 命名空间下独立安装的 pymatgen 扩展包括但不限于：通过 pymatgen-io-validation 验证 VASP [81] 计算是否与 Materials Project [5] 兼容；分别通过 pymatgen-io-aims、pymatgen-io-espresso 和 pymatgen-io-fleur 组织并解析 FHI-aims [18]、Quantum ESPRESSO [17] 和 FLEUR [82] 的电子结构计算；通过 pymatgen-io-openmm 组织使用 OpenMM [83] 的经典分子动力学计算；以及通过 pymatgen-analysis-defects [44] 提供核心缺陷功能。pymatgen 文档的附加组件部分维护着更完整的扩展包列表。

如图 4a 和图 4b 所示，十多年来，多个子软件包中的开发活动一直持续；贡献涉及错误修复与重构、结构与输入输出功能、测试与代码质量、文档，以及性能改进。

---

## 附件内容翻译

### Supporting Information（原 PDF 所附补充材料）

**AI 使用声明。** 各位合著者最初分别撰写了作者贡献声明草稿，随后使用 M365 Copilot 中的 GPT-5.6 统一表述，再由第一作者团队核查。补充材料的其他部分由 OpenAI Codex 使用中等推理级别的 gpt-5.6-sol 大语言模型起草。第一作者团队随后核实事实并校对文本，对其内容负责。

**范围。** 本补充材料说明正文各图所示数据如何收集和处理。分析源代码及缓存的中间数据见 https://github.com/janosh/pymatgen-2-paper。GitHub、OpenAlex 和 pymatgen 仓库都在持续变化；与文章关联的归档数据确定了图件使用的时间快照。

#### S1. OpenAlex 引文主题（正文图 1）

最初的 pymatgen 论文通过 OpenAlex 作品标识 W2015197254 确定。通过 OpenAlex Works API 查询引用该论文的作品，并按照各作品的 OpenAlex 主要主题分组。最多检索 50 个主题组，排除引用作品少于 10 篇的组。OpenAlex 数据于 2025 年 7 月 5 日前后获取。OpenAlex 主要主题由算法分配，因此后续的语言模型分组构成了第二层分类。

保留的主题名称及 OpenAlex 计数提供给 OpenAI 的 GPT-5 模型（gpt-5），要求模型以简洁标签将它们组织成五个主题分支。分支按其子主题计数之和排序，每个分支保留计数最高的四个子主题。模型返回的标签和计数被缓存为结构化数据，修订后的图件保留了这些缓存值。显示的 20 个子主题合计对应 2699 次引用作品的主题分配。这是选取的主题概览，并非对全部引文的穷尽划分。分支计数为所显示子节点之和；节点颜色和图例刻度共同采用范围从 1 到最大分支计数 1253 的对数 Viridis 色标。

#### S2. 影响范围层级（正文图 2）

仓库层面的数值于 2026 年 8 月从 materialsproject/pymatgen GitHub 仓库收集。276 位贡献者指截至 2025 年 12 月 31 日合并的非机器人 PR 的不同作者，与正文图 6 采用相同群体。GitHub 依赖关系图提供了 2713 个依赖仓库和 626 个依赖软件包的计数。这些值对应原始 pymatgen 仓库和软件包，而非 pymatgen-core。

合并的 PR 经 GitHub REST API 获取，按合并年份而非创建年份计数。机器人发起的 PR 通过以 `[bot]` 结尾的 GitHub 用户名识别，匹配时不区分大小写。逐年有无机器人 PR 的计数列于原文表格。

首次记录的 PR 合并发生在 2013 年 4 月 29 日；2013 年标记为 PR 活动不完整的年份，不计入年度平均值。在 2014—2025 年的 12 个日历年中，共合并 2454 个非机器人 PR，平均每年 204.5 个。

PyPI 下载计数来自 Google BigQuery 中公开的 PyPI 下载数据。2018 年 8 月至 2025 年 12 月合计 23,239,954 次，图中约记为 2320 万次。选择 2018 年 8 月作为起始月份，是因为 Python Packaging User Guide 指出，PyPI 下载数据管线在 2018 年 7 月 26 日之前显著低报总数。

Materials Project 的数值来自 Berkeley Lab 于 2026 年 1 月 13 日发布的一篇文章，其中报告每天约 5000 次使用和超过 65 万名注册用户。每日使用率换算为每年约 180 万次。

#### S3. 上游和下游软件包使用情况（正文图 3）

两幅图均通过静态分析 Python 文件和 Jupyter notebook 代码单元得到。对从软件包导入的 API 的调用进行计数，并通过导入别名解析。动态构建的调用未计入。连线宽度表示所得的函数调用次数。

##### S3.1 pymatgen 使用的依赖项 API（图 3a）

从 pymatgen 的 pyproject.toml 文件读取必需依赖项。分析的是 pymatgen 提交 `ab34799d8ab5dee80756489cf2ca28a97de78121` 的源代码。分别统计 alchemy、analysis、core、electronic_structure、entries、io、phonon、symmetry 和 transformations 子软件包中对各依赖项的调用。总调用次数少于 15 次的依赖项和子软件包未在图中显示。

##### S3.2 下游仓库使用的 pymatgen API（图 3b）

从 GitHub 的 pymatgen 依赖方页面收集仓库名称，通过 GitHub API 获取星标数，得到一张包含 1446 个仓库的表。按星标数从高到低选取仓库，直到保留 12 个；这些仓库来自归档表中星标数最高的 28 个仓库，每个至少有 127 颗星。16 个被排除的仓库中，8 个在测试之外不使用 pymatgen，或者只包含文档、课程或 Materials Project 内部材料；另 8 个在下述筛选之后 pymatgen 调用少于 10 次，例如 megnet 的 17 次调用中仅保留 8 次。所保留的各仓库均于 2026 年 9 月 26 日从默认分支进行浅克隆，对应提交列于原文表格。

分析 Python 文件和 notebook 代码时，排除了 tests、docs、.github 及隐藏路径。检测到的调用按导入路径中的第一个 pymatgen 子软件包分组。以 pymatgen.Structure、pymatgen.Molecule、pymatgen.MPRester、pymatgen.Composition 或 pymatgen.Element 开头的已弃用路径被舍弃。由于检测到的调用极少，分配给 pymatgen.phonon 的 5 次调用和 pymatgen.command_line 的 2 次调用也被舍弃。保留的 12 个仓库合计对应图中绘出的 914 次调用。

#### S4. 按主题与软件包统计的仓库开发活动（正文图 4）

##### S4.1 随时间变化的拉取请求主题（图 4a）

2026 年 9 月 8 日，通过分页的 GitHub REST API 收集 materialsproject/pymatgen 所有状态的拉取请求（PR）。图中包括 2026 年 1 月 1 日之前合并的全部 2494 个非机器人 PR，其中 167 个在完整的 2025 日历年内合并。排除 GitHub 标识为机器人，或用户名以 `[bot]` 结尾的账户，匹配时不区分大小写。每个 PR 编号仅保留一次，包括标题重复的 PR；年份是合并年份。

每个 PR 的标题直接通过按顺序执行、不区分大小写的正则表达式规则分类。第一次匹配的主题按以下顺序确定：文档；测试与代码质量；性能；错误修复与重构；输入输出与解析；结构与分析功能；无法匹配的归入“其他／未分类”。每个 PR 恰好分配一次，不对标题去重，也不从 LLM 生成的摘要推断计数。这些是基于标题的近似分类，并非经人工核实的 PR 内容描述。归档数据保留每个 PR 的编号、标题、作者、日期和所分配的主题，以供检查。

##### S4.2 软件包层面的提交活动（图 4b）

从 materialsproject/pymatgen 的 Git 历史中收集非合并提交，起点为 2011 年 10 月 23 日的初始提交 `fa7f41d8bd769a04cca1f78242ebf072664c871d`，终点为 2025 年 12 月 31 日。图中排除 2012 年 1 月 1 日之前的提交，因此显示 2012—2025 年的活动。统计 13 条选定路径：command_line、symmetry、alchemy、core/structure.py、core/periodic_table.py、io/vasp、transformations、analysis、optimization、electronic_structure、phonon、vis 和 entries。整个时期都匹配 pymatgen/ 与 src/pymatgen/ 路径；后者的目录布局于 2024 年 6 月 26 日采用。涉及每条路径的提交按月计数；从 2012 年 1 月起，再汇总为日历半年（1—6 月和 7—12 月）。同一提交若涉及多条选定路径，就分别计入每条对应路径一次。

#### S5. 按贡献者任期统计的拉取请求（正文图 5）

任期图使用与图 4a 相同的 2494 个非机器人已合并 PR，并按合并年份分组。检索所有状态的 PR，因此每位作者的首次提交日期包括未合并的 PR。任期是从首次提交到各已纳入 PR 的合并日期之间经过的时间，而非到 PR 创建日期之间的时间。

PR 被分入五个互不重叠的任期组：少于 7 天；7 天至不足 1 年；1 年至不足 3 年；3 年至不足 6 年；以及至少 6 年。一年定义为 365.25 天。包括截至 2025 年 12 月 31 日的全部合并记录。只表示 PR 活动，不计入审查、评论及其他贡献。

#### S6. 拉取请求贡献的地理分布（正文图 6）

使用 GitHub API 按作者统计已合并 PR，并获取各作者公开、自报的个人资料位置。排除 GitHub 用户名以 `[bot]` 结尾的账户，匹配时不区分大小写。使用 OpenStreetMap Nominatim 将自由文本位置解析为国家。对于公开的 pymatgen 团队页面中列出的、位置仍未确定的贡献者，使用 OpenAI 的 GPT-4o 模型将其所列单位映射为国家。另有部分映射经过人工整理。没有国家映射的贡献者不计入国家合计值。PR 计数和资料位置于 2026 年 2 月 16 日前后获取。

276 位贡献者中，124 位（44.9%）未在 GitHub 个人资料中提供位置。提供位置信息的 152 位贡献者全部被分配了国家，其中也包括通过人工整理的地理编码结果确定的国家。公开 pymatgen 团队页面列出的单位，以及人工整理的映射，为其余 124 位无资料位置的贡献者中的 57 位提供了国家信息。最终国家映射覆盖 209 位贡献者（75.7%）及 2498 个已合并 PR 中的 2362 个（94.6%）。剩余 67 位贡献者（24.3%）对应 136 个已合并 PR（5.4%），均无国家映射。

PR 计数按所映射国家求和。所得数值是已合并 PR 的数量，而不是不同贡献者的人数。贡献者的映射国家依据数据收集时使用的公开个人资料位置或所列单位确定。

#### S7. 源代码规模与测试覆盖率（正文图 7）

树图面积和覆盖率百分比均来自 2025 年 7 月 31 日生成的 coverage.py 7.6.12 JSON 快照，其中关闭了分支覆盖率。面积统计 src/pymatgen/ 下所报告 Python 文件中的可执行语句；无可执行语句的文件被排除，覆盖语句数为零的文件则保留。颜色表示覆盖语句数之和除以可执行语句数之和，父级软件包亦如此。报告记录 76,389 条可执行语句中有 60,242 条被覆盖（78.9%）。core 的覆盖率为 90.2%，entries 为 85.8%，io 为 83.6%，vis 为 13.9%。单元最多按三级路径组成分组；少于 1500 条语句的组合并入“其他”单元，少于 5000 条语句的子软件包显示为单个单元。没有使用单独安装的 pymatgen 源代码树确定面积；该图描述的是特定日期的测试套件快照。

#### S8. 贡献者与提交活动（正文图 8）

从 materialsproject/pymatgen 的 Git 历史中收集 2012 年 1 月 1 日至 2025 年 12 月 31 日的非合并提交元数据。排除合并提交；作者姓名以 `[bot]` 结尾的记录也被排除，匹配时不区分大小写。

若作者记录具有相同姓名，或其电子邮件地址转为小写后相同，则赋予同一个贡献者标识。非合并提交次数按 Git 作者日期汇总到各日历年。在某一年至少有一次非合并提交的贡献者，该年计为一名活跃贡献者。实线表示活跃贡献者人数，虚线表示同一年度非合并提交总次数。只计入 Git 提交历史中记录的活动。
