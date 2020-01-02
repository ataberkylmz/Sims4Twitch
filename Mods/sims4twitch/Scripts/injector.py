from functools import wraps
from sims4.localization import LocalizationHelperTuning
from ui.ui_dialog_notification import UiDialogNotification
from sims4.commands import Command, CheatOutput, CommandType
import inspect
import services

# method calling injection
def inject(target_function, new_function):
    @wraps(target_function)
    def _inject(*args, **kwargs):
        return new_function(target_function, *args, **kwargs)
    return _inject

# decarator injection.
def inject_to(target_object, target_function_name):
    def _inject_to(new_function):
        target_function = getattr(target_object, target_function_name)
        setattr(target_object, target_function_name, inject(target_function, new_function))
        return new_function
    return _inject_to

def is_injectable(target_function, new_function):
    target_argspec = inspect.getargspec(target_function)
    new_argspec = inspect.getargspec(new_function)
    return len(target_argspec.args) == len(new_argspec.args) - 1

def ft_show_notification(text, title=None):
    client = services.client_manager().get_first_client()
    if title is None:
        title = "Notification"
    _title = lambda **_: LocalizationHelperTuning.get_raw_text(title)
    _text = lambda **_: LocalizationHelperTuning.get_raw_text(text)
    notification = UiDialogNotification.TunableFactory().default(client.active_sim, text=_text, title=_title)
    notification.urgency = UiDialogNotification.UiDialogNotificationUrgency.DEFAULT
    notification.expand_behavior = UiDialogNotification.UiDialogNotificationExpandBehavior.FORCE_EXPAND
    notification.show_dialog(icon_override=(None, client.active_sim))
