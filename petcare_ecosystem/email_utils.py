from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def send_simple_email(subject, message, recipient_list, from_email=None):
    """
    Send a simple text email
    
    Args:
        subject: Email subject
        message: Email body (plain text)
        recipient_list: List of recipient email addresses
        from_email: Sender email (defaults to DEFAULT_FROM_EMAIL)
    
    Returns:
        Number of successfully sent emails
    """
    if from_email is None:
        from_email = settings.DEFAULT_FROM_EMAIL
    
    return send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False,
    )


def send_html_email(subject, text_content, html_content, recipient_list, from_email=None):
    """
    Send an HTML email with plain text fallback
    
    Args:
        subject: Email subject
        text_content: Plain text version of the email
        html_content: HTML version of the email
        recipient_list: List of recipient email addresses
        from_email: Sender email (defaults to DEFAULT_FROM_EMAIL)
    """
    if from_email is None:
        from_email = settings.DEFAULT_FROM_EMAIL
    
    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=from_email,
        to=recipient_list
    )
    email.attach_alternative(html_content, "text/html")
    email.send(fail_silently=False)


def send_welcome_email(user):
    """Send welcome email to new users"""
    subject = 'Welcome to Pet Care Ecosystem!'
    message = f"""
    Hi {user.get_full_name() or user.username},
    
    Welcome to Pet Care Ecosystem! We're excited to have you join our community.
    
    You can now:
    - Manage your pets' health records
    - Book veterinary appointments
    - Connect with other pet owners
    - Find adoption opportunities
    - And much more!
    
    Best regards,
    The Pet Care Ecosystem Team
    """
    
    return send_simple_email(
        subject=subject,
        message=message,
        recipient_list=[user.email]
    )


def send_appointment_confirmation(appointment):
    """Send appointment confirmation email"""
    subject = f'Appointment Confirmed - {appointment.clinic.name}'
    message = f"""
    Hi {appointment.user.get_full_name() or appointment.user.username},
    
    Your appointment has been confirmed!
    
    Details:
    - Clinic: {appointment.clinic.name}
    - Date & Time: {appointment.appointment_date.strftime('%B %d, %Y at %I:%M %p')}
    - Service: {appointment.service_type}
    - Pet: {appointment.pet.name if appointment.pet else 'Not specified'}
    
    Please arrive 10 minutes early.
    
    If you need to reschedule, please contact us as soon as possible.
    
    Best regards,
    {appointment.clinic.name}
    """
    
    return send_simple_email(
        subject=subject,
        message=message,
        recipient_list=[appointment.user.email]
    )


def send_adoption_application_notification(application):
    """Notify listing owner about new adoption application"""
    subject = f'New Adoption Application for {application.listing.pet_name}'
    message = f"""
    Hi {application.listing.owner.get_full_name() or application.listing.owner.username},
    
    You have received a new adoption application!
    
    Applicant: {application.applicant.get_full_name() or application.applicant.username}
    Pet: {application.listing.pet_name}
    
    Please review the application and respond at your earliest convenience.
    
    Best regards,
    Pet Care Ecosystem Team
    """
    
    return send_simple_email(
        subject=subject,
        message=message,
        recipient_list=[application.listing.owner.email]
    )


def send_lost_pet_alert(report):
    """Send alert about lost pet report"""
    subject = f'Lost Pet Alert: {report.pet_name}'
    message = f"""
    A pet has been reported lost in your area!
    
    Pet Name: {report.pet_name}
    Species: {report.species}
    Breed: {report.breed}
    Last Seen: {report.last_seen_location}
    Date: {report.last_seen_date.strftime('%B %d, %Y')}
    
    Description: {report.description}
    
    Contact: {report.contact_phone}
    
    If you have any information, please contact the owner immediately.
    
    Best regards,
    Pet Care Ecosystem Team
    """
    
    return send_simple_email(
        subject=subject,
        message=message,
        recipient_list=[report.reporter.email]
    )
