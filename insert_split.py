import re

with open('section_split_processing_draft.md', 'r') as f:
    draft = f.read()

def md_to_tex(text):
    # Convert ### to \subsection (or \subsubsection if needed)
    # The user wanted it in 2.2.4, which is a subsection of 2.2
    # But looking at others, 2.2.3 was \subsection{Hardware Architectures for AI (PEPR CAMELIA)}
    # Let me check what HDR TEX uses. It uses \subsection{...}
    text = re.sub(r'^###\s+.*?\[NOUVEAU\]\s+(.*?)$', r'\\subsection{\1}', text, flags=re.MULTILINE)
    text = re.sub(r'^###\s+(.*?)$', r'\\subsection{\1}', text, flags=re.MULTILINE)
    # Convert **bold** to \textbf{bold}
    text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)
    # Convert bullets
    text = re.sub(r'(?m)^(\s*)\*\s+(.*?)$', r'\\begin{itemize}\n\1\\item \2\n\\end{itemize}', text)
    # Merge itemize blocks
    text = re.sub(r'\\end\{itemize\}\s*\\begin\{itemize\}', '', text)
    # Convert numbered lists
    text = re.sub(r'(?m)^(\s*)\d+\.\s+(.*?)$', r'\\begin{enumerate}\n\1\\item \2\n\\end{enumerate}', text)
    # Merge enumerate blocks
    text = re.sub(r'\\end\{enumerate\}\s*\\begin\{enumerate\}', '', text)
    return text

tex_content = md_to_tex(draft) + "\n\n"

with open('hdr.tex', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.strip() == r'\appendix':
        lines.insert(i, tex_content)
        break

with open('hdr.tex', 'w') as f:
    f.writelines(lines)
