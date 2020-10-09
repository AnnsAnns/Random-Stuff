#pragma once

#include <cmath>

class PID {
public:
    constexpr PID(double kp, double ki, double kd) noexcept : m_kp(kp), m_ki(ki), m_kd(kd) { }

    [[nodiscard]] constexpr double update(double currValue, double target) noexcept {
        const double error = target - currValue;
        const double output = this->m_kp * error + this->m_ki * this->m_integral + this->m_kd * (error - this->m_prevError);
        
        this->m_integral += error;
        this->m_prevError = error;

        return output;
    }

private:
    const double m_kp, m_ki, m_kd;
    double m_prevError = 0;
    double m_integral = 0;
};
