class ExternalAmplifierConfig:
    delay_amplifier = None
    delay_speakers = None
    gpio_amplifier = None
    gpio_speakers = None

    def __init__(self, gpio_amplifier, gpio_speakers, delay_amplifier=2, delay_speakers=1):
        self.gpio_amplifier = gpio_amplifier
        self.gpio_speakers = gpio_speakers
        self.delay_amplifier = delay_amplifier
        self.delay_speakers = delay_speakers
