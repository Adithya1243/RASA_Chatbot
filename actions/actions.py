from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionProvideEmploymentLink(Action):

    def name(self) -> Text:
        return "action_provide_employment_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="You can find more information and apply https://www.morrisvillenc.gov/government/departments-services/human-resources. Anything else I can help you with?")

        return []

class ActionListServices(Action):

    def name(self) -> Text:
        return "action_list_services"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="What can I help you with? I can provide information on athletics, school programs & camps, aquatics and fitness center, senior center, facility rentals, cultural events.")

        return []

class ActionProvideSpecificInfoLink(Action):

    def name(self) -> Text:
        return "action_provide_specific_info_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        last_message = tracker.latest_message.get('text').lower()

        if "athletics" in last_message:
            link = "https://www.morrisvillenc.gov/government/departments-services/parks-recreation-cultural-resources/athletics"
        elif "school programs and camps" in last_message:
            link = "https://www.morrisvillenc.gov/government/departments-services/parks-recreation-cultural-resources/cedar-fork-community-center"
        elif "cultural events" in last_message:
            link = "https://www.morrisvillenc.gov/government/departments-services/parks-recreation-cultural-resources/special-events"
        elif "facility rentals" in last_message:
            link = "https://www.morrisvillenc.gov/government/departments-services/parks-recreation-cultural-resources/facility-rentals"
        elif "aquatics" in last_message:
            link = "https://www.morrisvillenc.gov/government/departments-services/parks-recreation-cultural-resources/morrisville-aquatics-and-fitness-center"
        elif "senior center":
            link = "https://www.morrisvillenc.gov/recreation/parks-recreation-cultural-resources/morrisville-senior-center"
        else:
            link = "For more information, please visit our website."

        dispatcher.utter_message(text=f"You can find more information at {link}. Anything else I can help you with?")

        return []


# For IT and Planning
    
class ActionProvideITLink(Action):
    def name(self) -> Text:
        return "action_provide_it_link"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="You can find more information about our Information Technology services at https://www.morrisvillenc.gov/government/departments-services/information-technology.")
        return []

class ActionAskPlanningSpecific(Action):
    def name(self) -> Text:
        return "action_ask_planning_specific"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Is there anything specific you're interested in? We offer information on Transit-oriented development, affordable housing, development information, long-range planning, permits and applications, transportation planning, smart shuttle maps, and the unified development ordinance.")
        return []

class ActionProvidePlanningInfoLink(Action):
    def name(self) -> Text:
        return "action_provide_planning_info_link"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        last_message = tracker.latest_message.get('text').lower()
        # Example for handling one specific topic, extend as needed
        if "affordable housing" in last_message:
            link = "https://www.morrisvillenc.gov/government/departments-services/planning/affordable-housing"
        else:
            link = "Please visit our planning section for more information."
        dispatcher.utter_message(text=f"You can find more information at {link}. Anything else I can help you with?")
        return []
    