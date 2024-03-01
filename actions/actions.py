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
        dispatcher.utter_message(text="You can find more information and apply at https://www.morrisvillenc.gov/government/departments-services/human-resources. Anything else I can help you with?")
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
        service = next(tracker.get_latest_entity_values("service"), None)
        links = {
            "athletics": "https://www.morrisvillenc.gov/government/departments-services/parks-recreation-cultural-resources/athletics",
            "senior center": "https://www.morrisvillenc.gov/recreation/parks-recreation-cultural-resources/morrisville-senior-center",
            "aquatics": "https://www.morrisvillenc.gov/government/departments-services/parks-recreation-cultural-resources/morrisville-aquatics-and-fitness-center",
            # Add other services and their links here
            "school programs and camps":"https://www.morrisvillenc.gov/government/departments-services/parks-recreation-cultural-resources/cedar-fork-community-center",
            "cultural events":"https://www.morrisvillenc.gov/government/departments-services/parks-recreation-cultural-resources/special-events",
            "facility rentals":"https://www.morrisvillenc.gov/government/departments-services/parks-recreation-cultural-resources/facility-rentals"
        }
        if service in links:
            dispatcher.utter_message(text=f"You can find more information about {service} at {links[service]}. Anything else I can help you with?")
        else:
            dispatcher.utter_message(text="For more information, please visit our website.")
        return []

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
        planning_topic = next(tracker.get_latest_entity_values("planning_topic"), None)
        links = {
            "affordable housing": "https://www.morrisvillenc.gov/government/departments-services/planning/affordable-housing",
            # Add other planning topics and their links here
            "transit":"https://www.morrisvillenc.gov/government/departments-services/planning/long-range-planning/transit-oriented-development/-fsiteid-1#!/",
            "development":"https://www.morrisvillenc.gov/government/departments-services/planning/long-range-planning/transit-oriented-development/-fsiteid-1#!/",
            "long range planning":"https://www.morrisvillenc.gov/government/departments-services/planning/long-range-planning/transit-oriented-development/-fsiteid-1#!/",
            "permits":"https://www.morrisvillenc.gov/government/departments-services/planning/long-range-planning/transit-oriented-development/-fsiteid-1#!/",
            "transportation":"https://www.morrisvillenc.gov/government/departments-services/planning/long-range-planning/transit-oriented-development/-fsiteid-1#!/",
            "smart shuttle":"https://www.morrisvillenc.gov/government/departments-services/planning/long-range-planning/transit-oriented-development/-fsiteid-1#!/",
            "maps":"https://www.morrisvillenc.gov/government/departments-services/planning/long-range-planning/transit-oriented-development/-fsiteid-1#!/"
        }
        if planning_topic in links:
            dispatcher.utter_message(text=f"You can find more information about {planning_topic} at {links[planning_topic]}. Anything else I can help you with?")
        else:
            dispatcher.utter_message(text="Please visit our planning section for more information.")
        return []
