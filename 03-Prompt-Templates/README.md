
# 03 - Prompt Templates

## 📚 What I Learned

In this section, I explored how LangChain manages prompts and how they can be structured to build more reliable and reusable AI applications.

### Concepts Covered

- Understanding prompts and their role in interacting with Large Language Models (LLMs).
- Difference between deterministic and creative outputs using the **temperature** parameter.
- Static vs. Dynamic Prompts.
- Creating reusable prompts with **Prompt Templates**.
- Saving and reusing prompt templates.
- Understanding different message types:
  - System Message
  - Human Message
  - AI Message
- Building conversations using **Chat Prompt Templates**.
- Using **Message Placeholders** to insert chat history dynamically.
- Learned how prompt engineering forms the foundation of conversational AI systems.

---

## 📂 Files

| File | Description |
|------|-------------|
| `prompt_template_tutorial.py` | Introduction to Prompt Templates and dynamic prompts. |
| `chat_prompt_template_tutorial.py` | Working with System, Human, and AI messages using ChatPromptTemplate. |
| `message_placeholder_tutorial.py` | Using MessagePlaceholder to inject conversation history into prompts. |

---

## 💡 Key Takeaways

- Prompt Templates make prompts reusable instead of hardcoding strings.
- ChatPromptTemplate helps structure conversations in a clean and scalable way.
- System messages define the assistant's behavior.
- Human messages represent user input.
- AI messages store previous model responses.
- MessagePlaceholder enables chat history, which is essential for stateful AI assistants.

---

## 🚀 Reflection

Before this topic, I thought prompting simply meant writing better instructions for an LLM. After learning LangChain's prompting system, I realized prompts can be designed as reusable components that make AI applications cleaner, more maintainable, and easier to scale.

---

## 🛠 Skills Practiced

- Prompt Engineering
- PromptTemplate
- ChatPromptTemplate
- System Messages
- Human Messages
- AI Messages
- MessagePlaceholder
- LangChain Core
