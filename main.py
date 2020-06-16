import weather, notification

RAIN_LIKELY_THRESHOLD = -2

rain_obj = weather.get_rain_data()
if rain_obj['rain_probability'] > RAIN_LIKELY_THRESHOLD:
    notification.send_alert_message(rain_obj['rain_probability'])