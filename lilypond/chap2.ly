\version "2.17.2"

% bar lines and check
\relative c {
    \clef "bass" g1 e1 \bar "||" b'2. c'4 \bar "|."
}

% accidentals
\relative c {
  \clef "bass" cis4 fes aeses
}

% key signature
\relative c {
  \clef "bass"
  \key d \major a1 |
  \key c \minor a1 |
}

% pitch and key signature
\relative c'' {
  \key d \major
  cis4 d e fis f
}
