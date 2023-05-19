from source.questions.question5.FormationTypes import FormationType
from rx.subject import Subject


class Group:
    def __init__(self):
        self._formation_type = FormationType.Sectorial
        self._formation_type_value_property_changed = Subject()
        self._is_phased_array = True

    @property
    def _is_phased_array(self):
        return self._is_phased_array

    @_is_phased_array.setter
    def _is_phased_array(self, value: bool):
        if value != self._is_phased_array:
            self._formation_type_value_property_changed.on_next(value)
            self._is_phased_array = value

    def subscribe_formation_type_changed_changed_event(self, on_value_change):
        self._formation_type_value_property_changed.subscribe(
            on_next=lambda new_value: on_value_change(new_value, self._is_phased_array),
            on_error=lambda e: print(
                "Error on di_value_changed_observable : {0}".format(e)),
            on_completed=lambda: print("Job Done!"))

    def dispose(self):
        self._formation_type_value_property_changed.dispose()
        return True
