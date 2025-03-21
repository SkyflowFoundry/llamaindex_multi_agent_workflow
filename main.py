from workflows.multi_agent_workflow import MultiAgentWorkflow

if __name__ == "__main__":
    workflow = MultiAgentWorkflow()
    input_text = "Rachel is your NSIGHT Health AI Care Manager. She is trying to call the patient to check on their condition. Give me 3 ways to take care of your health."
    output = workflow.run(input_text)
    print(output)
