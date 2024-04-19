from configcraft.model import query_rewrite_agent, iptables_agent

def get_ai_response(input_text: str):
    print(f"Received query: {input_text}")
    # enhanced_query = str(query_rewrite_agent.chat(
    #     input_text
    # ))
    # print(f"Enhanced query: {enhanced_query}")
    response = iptables_agent.chat(input_text)
    return str(response)