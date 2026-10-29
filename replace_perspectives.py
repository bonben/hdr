import re

with open('hdr.tex', 'r') as f:
    content = f.read()

# We identify the block to replace: from "\section{Network Specialization for Embedded Targets}" to "\appendix"
start_str = r"\\section\{Network Specialization for Embedded Targets\}"
end_str = r"\\appendix"

# We read the newly created drafts
with open('section_2_2_1_draft.md', 'r') as f:
    draft1 = f.read()
with open('section_2_2_new_hardware_draft.md', 'r') as f:
    draft2 = f.read()
with open('section_2_2_2_draft.md', 'r') as f:
    draft3 = f.read()

# Helper function to convert simple Markdown to LaTeX
def md_to_tex(text):
    # Convert # to \subsection
    text = re.sub(r'^#\s+(.*?)$', r'\\subsection{\1}', text, flags=re.MULTILINE)
    # Convert ## to \subsubsection
    text = re.sub(r'^##\s+(.*?)$', r'\\subsubsection{\1}', text, flags=re.MULTILINE)
    # Convert bullets
    text = re.sub(r'(?m)^(\s*)\*\s+(.*?)$', r'\\begin{itemize}\n\1\\item \2\n\\end{itemize}', text)
    # Merge adjacent itemize blocks
    text = re.sub(r'\\end\{itemize\}\s*\\begin\{itemize\}', '', text)
    # Convert bold
    text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)
    return text

new_content_md = draft1 + "\n\n" + draft2 + "\n\n" + draft3
new_content_tex = "\\section{Network Specialization for Embedded Targets}\n\n" + md_to_tex(new_content_md)

# In the current draft, we also have section 2.1.3 embedded in section 2.1. Let's just replace the 2.2 part for now to be safe and match the plan
pattern = re.compile(f"({start_str}.*?)({end_str})", re.DOTALL)

if pattern.search(content):
    modified = pattern.sub(f"{new_content_tex.replace('\\', '\\\\')}\n\n\\2", content)
    with open('hdr.tex', 'w') as f:
        f.write(modified)
    print("Successfully replaced content.")
else:
    print("Could not find the target section.")
