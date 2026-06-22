def generate_summary_prompt(
    summary_type,
    context
):

    prompts = {

        "executive": f"""
You are an expert research paper analyst.

Generate an Executive Summary.

Include:
1. Objective
2. Main Contribution
3. Methodology
4. Results
5. Conclusion

Context:
{context}
""",

        "methodology": f"""
Explain the methodology used in this research paper.

Include:
- Approach
- Models
- Algorithms
- Workflow

Context:
{context}
""",

        "results": f"""
Summarize the experimental results.

Include:
- Dataset
- Metrics
- Findings
- Performance

Context:
{context}
""",

        "limitations": f"""
Identify limitations discussed in the paper.

Context:
{context}
""",

        "future_work": f"""
Identify future work opportunities mentioned in the paper.

Context:
{context}
"""
    }

    return prompts[summary_type]