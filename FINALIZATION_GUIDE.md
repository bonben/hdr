# HDR Document Finalization & Perspectives Guide

This document aggregates all the necessary tasks to finalize your Habilitation à Diriger des Recherches (HDR) document, along with a comprehensive strategy to expand and strengthen the "Research Perspectives" chapter.

---

## Part 1: Tasks to Finalize the Document

### 1.1 Content & Structure
- [ ] **Research Perspectives Expansion**: Expand the draft sections (`section_2_1_1_draft.md`, `section_2_1_agentic_draft.md`, `section_2_2_1_draft.md`, `section_2_2_2_draft.md`) using the advice in Part 2 below, and integrate them into Chapter 3 of `hdr.tex`.
- [ ] **Address TODO Markers**:
  - `hdr.tex:1274`: `\textcolor{red}{Ajouter intro sur les réseaux et la compression ?}` — Write this introduction or remove the marker if already covered.
  - `hdr.tex:542`: `%TODO citations mcgill & nous` — Verify and add the missing citations.
- [ ] **Fill Placeholders**:
  - The **Jury / Committee definitions** on the title page (e.g., `\jurynameA`, `\juryroleA`) currently contain placeholders and need to be finalized with actual names.
  - The "Spotlight on two courses" section (line 2177) is currently empty. Add content or remove the section.
- [ ] **Appendix Consistency**: Review the CV appendices (`main_french.pdf` and `enseignements.pdf`) to ensure they seamlessly fit the final English document.

### 1.2 Form & Formatting
- [ ] **Language Consistency (Translate to English)**:
  - `hdr.tex:245`: Caption `Duplication de l'arbre de décodage dans l'algorithme SCL.`
  - `hdr.tex:350`: Caption `Comparaison de débits et latences des algorithmes SCL adaptatifs pour des représentations à virgule flottante (32 bits) et virgule fixe (16 et 8 bits).`
  - Table 2.2 Headers (`hdr.tex:354`): Translate "Décodeur" and "Quantif."
- [ ] **Correct Typos**:
  - `hdr.tex:2026`: Fix the typo `\paragraph{Compraison with other hardware implementations}` to `Comparison`.
- [ ] **Fix LaTeX Warnings & Layout Issues**:
  - Remove or name the **empty labels**: `\label{}` found at lines 648 and 769.
  - **Float Size Warnings**: Several figures/tables are too large for the page (e.g., lines 1646 and 1711).
  - **Floats Placement**: `h` float specifiers have been automatically changed to `ht`; consider switching to `[htp]` or `[htbp]`.

### 1.3 Bibliography & References
- [ ] **Resolve Missing Citations**:
  - `blott2018finnr` (Line 1916)
  - `Umuroglu_2017` (Line 1916)
  - `brevitas` (Line 1918)
  - `vinyals2016matching` (Line 2008)
- [ ] **Fix Bibliography Splits / Keywords**:
  - `Keyword 'WORKSHOP' not found` at line 2189, resulting in an empty "Communications without Proceedings" section. Ensure the `.bib` file tags these entries correctly or adjust the `<keyword>` field in the `\printbibliography` command.
  - Review the split bibliography warnings and ensure they are rendering correctly in the final PDF.

---

## Part 2: Strategy for a Longer & Stronger "Perspectives" Chapter

The Perspectives chapter is often considered the most critical part by the jury, as it proves your ability to secure funding and lead a research group. Treat it like a major grant proposal (ANR or ERC). Here is how to expand your current drafts:

### 2.1 Structure by Timeline: Short, Medium, and Long-Term
Instead of just presenting the topic, break each research axis into chronological phases. This adds volume and demonstrates strategic planning:
*   **Short-term (1-2 years)**: Direct continuations of your current PhD students (Timotée, Ismail, Jérémy, Elise). Detail the logical next steps once they defend.
*   **Medium-term (3-5 years)**: The core of your future proposals. What new projects will you submit? What are the intermediate hurdles?
*   **Long-term (5-10 years)**: The ambitious, paradigm-shifting goals (e.g., the "Self-Optimizing Modem for 6G" and "Always-On Neuro-Wearables").

### 2.2 Deepen the State of the Art (SOTA)
For each perspective, add 1-2 pages of focused literature review.
*   **Identify the "Wall"**: Clearly explain the exact limitations of current approaches. For example, in the "Agentic Paradigm" section, detail exactly why current NAS or HLS tools fail at *inventing* architectures, citing 4-5 recent influential papers.
*   This proves that your perspective isn't just a "good idea", but a scientifically necessary next step.

### 2.3 Detail the Methodology (Think "Work Packages")
Break down *how* you will achieve these goals. Formulate them as Work Packages (WPs).
*   **Experimental Protocol**: What specific datasets will you use? Which specific MCU/FPGA development boards?
*   **Technical Challenges**: For example, in the EEG/Mamba perspective, detail *how* you plan to perform the tiling/vectorization. What are the specific memory constraints of the targeted ARM CMSIS-NN?

### 2.4 Add a "Risk Analysis and Mitigation" Section
Juries value this because it demonstrates maturity and foresight. For every major scientific goal, include:
*   **Scientific Risks**: What if the LLM in your evolutionary algorithm cannot converge on a synthesisable instruction? What if the Linear Attention mechanism loses too much accuracy on EEG data?
*   **Fallback Plans (Plan B)**: How will you pivot if the main idea fails? (e.g., restricting the LLM to a highly constrained domain-specific language instead of raw C++).

### 2.5 Specify Human Resources and Funding Strategy
An HDR authorizes you to supervise research. You must explain *how* you will staff and fund these future axes.
*   **Staffing**: Specify the profiles you need. (e.g., *"Axis 1 will require funding a PhD student with a dual background in compiler design and deep learning..."*).
*   **Funding Targets**: Explicitly name the grants you plan to apply for. Mention specific ANR calls (e.g., AAPG, PEPR Networks of the Future), European grants (ERC Consolidator, Horizon Europe clusters), or future CIFRE partnerships.

### 2.6 Detail Collaborations and Networks
You briefly mention collaborations (e.g., Giulia Lioi for EEG, Tohoku University). Expand on these:
*   What complementary skills do they bring to the table?
*   How will the collaboration function? (Co-supervision of PhDs, visiting scholar programs, shared experimental platforms).

### 2.7 Emphasize Societal, Ecological, and Economic Impact
Dedicate a full subsection at the end of the chapter to the broader impacts of your future work:
*   **Green AI / Frugality**: Connect your MCU/FPGA hardware co-design to the reduction of the carbon footprint of AI.
*   **Sovereignty**: Emphasize how the GNSS anti-jamming and European open-source hardware (RISC-V) contribute to technological independence.
*   **Valorization**: Mention any plans for technology transfer, patents, or startup creation, leveraging your past experiences (e.g., GoodFloow, DeepLite).
