from rx.subject import Subject
from source.questions.question5.FormationTypes import FormationType
from source.questions.question5.Group import Group


class EndScan:

    def __init__(self, group: Group):
        self._group = group
        self.is_group_TFM_value_property_changed = Subject()
        self._is_group_TFM = group._formation_type == FormationType.TFM

    @property
    def is_group_TFM(self):
        return self._is_group_TFM

    @is_group_TFM.setter
    def is_group_TFM(self, value: bool):
        if value != self._is_group_TFM:
            self.is_group_TFM_value_property_changed.on_next(value)
            self._is_group_TFM = value

    def set_group(self, new_group: Group):
        self._group = new_group
        self._is_group_TFM = new_group._formation_type == FormationType.TFM

    def subscribe_is_group_TFM_changed_event(self, on_value_change):
        self.is_group_TFM_value_property_changed.subscribe(
            on_next=lambda new_value: on_value_change(new_value, self.is_group_TFM),
            on_error=lambda e: print(
                "Error on di_value_changed_observable : {0}".format(e)),
            on_completed=lambda: print("Job Done!"))

    def dispose(self):
        self.is_group_TFM_value_property_changed.dispose()
        return True
