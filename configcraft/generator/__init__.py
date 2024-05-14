from configcraft.model import iptables_agent, soot_agent, general_agent

def get_ai_response(input_text: str, target: str):
    print(f"Received query: {input_text}")
    # enhanced_query = str(query_rewrite_agent.chat(
    #     input_text
    # ))
    # print(f"Enhanced query: {enhanced_query}")
    if target == "iptables":
        response = iptables_agent.chat(input_text)
    elif target == "soot":
        response = soot_agent.chat(input_text)
    elif target == "(Not Specified)":
        response = general_agent.chat(input_text)
    return str(response)