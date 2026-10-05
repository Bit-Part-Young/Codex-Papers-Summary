# 论文总结约定

本项目用于总结与翻译材料科学、凝聚态物理论文。具体内容和格式规则见 `.codex/skills/paper-summarize/SKILL.md`。

- 用户消息只包含一个或多个 PDF（文件路径、`@` 引用或附件），没有其他任务文字时，直接使用 `paper-summarize` skill 完成论文总结与翻译，无需追问或确认。
- 用户要求翻译指定章节、段落、图题、表题或附件时，使用同一 skill。若当前对话已为该论文生成 `2-summaries/` 下的总结文件，将译文追加到该文件，保留已有内容，不另建文件。
- 总结文件统一写入 `2-summaries/`。`map_codex_paper_sessions.py` 后续按 Codex 对话名称重映射并复制文件；不要直接将新总结写入 `3-summaries-renamed/`。
