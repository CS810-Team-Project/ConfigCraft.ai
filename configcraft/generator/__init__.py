from configcraft.model import iptables_agent, soot_agent, general_agent

def get_ai_response(input_text: str, target: str, model: str):
    print(f"Received query: {input_text}")
    # enhanced_query = str(query_rewrite_agent.chat(
    #     input_text
    # ))
    # print(f"Enhanced query: {enhanced_query}")
    if model == "OpenAI":
        if target == "iptables":
            response = iptables_agent.chat(input_text)
        elif target == "soot":
            response = soot_agent.chat(input_text)
        elif target == "(Not Specified)":
            response = general_agent.chat(input_text)
        return str(response)
    elif model == "Codellama":
        return "See jupyter notebook files: `experimental/rag_iptables.ipynb and experimental/rag_soot2.ipynb` for more details."
    else:
        # error
        return "Invalid model selected"