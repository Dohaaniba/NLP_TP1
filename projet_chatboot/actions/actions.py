class ActionInform(Action):
    def name(self) -> Text:
        return "action_inform"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        age = tracker.get_slot("age")

        if name and age:
            message = f"Bonjour {name}, vous avez {age} ans."
        elif name:
            message = f"Bonjour {name}."
        elif age:
            message = f"Vous avez {age} ans."
        else:
            message = "Je n'ai pas reçu d'information sur le nom ou l'âge."

        dispatcher.utter_message(text=message)
        return []
