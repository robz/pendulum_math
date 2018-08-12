const θ1DotDot =
  ((L1 * m2 * sin(2 * θ2) * θ1Dot ** 2) / 2 +
    L2 * m2 * sin(θ2) * θ1Dot ** 2 +
    2 * L2 * m2 * sin(θ2) * θ1Dot * θ2Dot +
    L2 * m2 * sin(θ2) * θ2Dot ** 2 -
    g * m1 * sin(θ1) +
    (g * m2 * sin(θ1 + 2 * θ2)) / 2 -
    (g * m2 * sin(θ1)) / 2) /
  (L1 * (m1 + m2 * sin(θ2) ** 2));
const θ2DotDot =
  -(
    L1 * sin(θ2) * θ1Dot ** 2 +
    L1 * cos(θ2) * θ1DotDot +
    L2 * θ1DotDot +
    g * sin(θ1 + θ2)
  ) / L2;
