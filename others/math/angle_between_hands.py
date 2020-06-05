class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_hand = (30 * (hour % 12)) + (minutes / 2)
        minute_hand = 6 * minutes
        diff = max(hour_hand, minute_hand) - min(hour_hand, minute_hand)
        return min(diff, 360 - diff)

    class Solution:
        def angleClock(self, hour: int, minutes: int) -> float:
            if hour == 12:
                degh = (12 - hour) * 30 + (minutes * 0.5)
                degm = minutes * 6
            else:
                degh = (hour * 30) + (minutes * 0.5)
                degm = minutes * 6
            diff = max(degh, degm) - min(degh, degm)
            return min(diff, 360 - diff)
