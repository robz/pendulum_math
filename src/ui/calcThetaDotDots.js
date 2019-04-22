const { sin, cos } = Math;
const g = 9.8;
function calcThetaDotDots(
  { theta1, theta2, theta1Dot, theta2Dot },
  { L1, L2, m1, m2 },
  { F }
) {
  const theta1DotDot =
    ((1 / 2) * L1 * m1 * Math.pow(theta1Dot, 2) * sin(2 * theta1) -
      m1 * (L1 * Math.pow(theta1Dot, 2) * cos(theta1) + g) * sin(theta1) +
      m2 *
        (L1 * Math.pow(theta1Dot, 2) * cos(theta2) +
          L2 * Math.pow(theta1Dot, 2) +
          2 * L2 * theta1Dot * theta2Dot +
          L2 * Math.pow(theta2Dot, 2) +
          g * cos(theta1 + theta2)) *
        sin(theta2)) /
    (L1 * (m1 + m2 * Math.pow(sin(theta2), 2)));
  const theta2DotDot =
    F / (L2 * m2) -
    (L1 * Math.pow(theta1Dot, 2) * sin(theta2)) / L2 -
    (L1 * theta1DotDot * cos(theta2)) / L2 -
    theta1DotDot -
    (g * sin(theta1 + theta2)) / L2;
  return { theta1DotDot, theta2DotDot };
}
