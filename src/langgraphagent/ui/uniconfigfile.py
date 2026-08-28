from configparser import ConfigParser

class Config:
    def __init__(self, config_file = "src/langgraphagent/ui/uiconfigfile.ini"):
        self.config_file = config_file
        self.parser = ConfigParser()
        self.parser.read(self.config_file)

    def get_llm_model(self):
        #return self.parser.get("DEFAULT", "LLM_MODEL")
        return self.parser["DEFAULT"].get("LLM_MODEL").split(",")

    def get_usecase_options(self):
        return self.parser["DEFAULT"].get("USECASE_OPTIONS").split(",")

    def get_page_title(self):
        return self.parser["DEFAULT"].get("PAGE_TITLE")
    def get_from_model(self):
        return self.parser["DEFAULT"].get("FROM_MODEL")