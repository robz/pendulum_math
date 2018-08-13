const θ1DotDot =
  ((L1 * m1 * sin(2 * θ1) * θ1Dot ** 2) / 2 -
    m1 * (L1 * cos(θ1) * θ1Dot ** 2 + g) * sin(θ1) +
    m2 *
      (L1 * cos(θ2) * θ1Dot ** 2 +
        L2 * θ1Dot ** 2 +
        2 * L2 * θ1Dot * θ2Dot +
        L2 * θ2Dot ** 2 +
        g * cos(θ1 + θ2)) *
      sin(θ2)) /
  (L1 * (m1 + m2 * sin(θ2) ** 2));
const θ2DotDot =
  -(
    L1 * sin(θ2) * θ1Dot ** 2 +
    L1 * cos(θ2) * θ1DotDot +
    L2 * θ1DotDot +
    g * sin(θ1 + θ2)
  ) / L2;
