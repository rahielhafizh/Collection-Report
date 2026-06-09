from typing import List, Union
from services.mailer.outlook_mailer_core import MailerProfile, OutlookMailer

_PROFILE = MailerProfile(
    name="SUMMARY MONITORING MOBCOLL",
    submission_config_key="SUBMISSION_MOBCOLL",
)


def send_outlook_email(
    outlook_recipients: Union[str, List[str]],
    secondary_recipients: Union[str, List[str]],
    subject_email: str,
    core_email: str,
    footer_template: str,
) -> None:
    OutlookMailer(_PROFILE).send(
        to=outlook_recipients,
        cc=secondary_recipients,
        subject=subject_email,
        body=core_email,
        footer=footer_template,
    )
