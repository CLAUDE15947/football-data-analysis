-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 14 mars 2025 à 14:10
-- Version du serveur : 10.4.27-MariaDB
-- Version de PHP : 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `footballstats`
--

-- --------------------------------------------------------

--
-- Structure de la table `stats_equipes`
--

CREATE TABLE `stats_equipes` (
  `classement` int(11) NOT NULL,
  `equipe` varchar(255) DEFAULT NULL,
  `competition` varchar(255) DEFAULT NULL,
  `buts` int(11) DEFAULT NULL,
  `tirs_match` float DEFAULT NULL,
  `cartons_jaunes` int(11) DEFAULT NULL,
  `cartons_rouges` int(11) DEFAULT NULL,
  `possession` float DEFAULT NULL,
  `passes_reussies` float DEFAULT NULL,
  `duels_aeriens_gagnes` float DEFAULT NULL,
  `note` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `stats_equipes`
--

INSERT INTO `stats_equipes` (`classement`, `equipe`, `competition`, `buts`, `tirs_match`, `cartons_jaunes`, `cartons_rouges`, `possession`, `passes_reussies`, `duels_aeriens_gagnes`, `note`) VALUES
(1, '1. Paris Saint-Germain', 'Ligue 1', 70, 18.6, 31, 0, 68.6, 91, 8.1, 7.02),
(2, '2. Bayern Munich', 'Bundesliga', 74, 18.9, 38, 1, 69.2, 90.2, 12.6, 6.98),
(3, '3. Barcelona', 'LaLiga', 71, 17.2, 43, 3, 67.8, 88, 10, 6.88),
(4, '4. Liverpool', 'Premier League', 69, 17, 54, 2, 57.2, 86.3, 10.8, 6.87),
(5, '5. Real Madrid', 'LaLiga', 57, 16.2, 44, 3, 60.8, 89.9, 8, 6.86),
(6, '6. Arsenal', 'Premier League', 52, 13.9, 53, 5, 56.5, 86.6, 13.4, 6.79),
(7, '7. Inter', 'Serie A', 63, 16, 36, 0, 60, 88.2, 17, 6.79),
(8, '8. Atalanta', 'Serie A', 63, 15, 49, 0, 56.1, 85.8, 15.5, 6.79),
(9, '9. Bayer Leverkusen', 'Bundesliga', 55, 16, 44, 1, 59.3, 87.4, 13.2, 6.78),
(10, '10. Bournemouth', 'Premier League', 47, 16, 71, 1, 46.6, 79, 14.8, 6.76),
(11, '11. Monaco', 'Ligue 1', 49, 15.2, 42, 3, 55.8, 83.2, 13.3, 6.76),
(12, '12. Nice', 'Ligue 1', 49, 14, 43, 3, 46.6, 83.8, 12.4, 6.76),
(13, '13. Mainz 05', 'Bundesliga', 42, 11.7, 55, 3, 49.2, 77.9, 19.1, 6.75),
(14, '14. Manchester City', 'Premier League', 53, 16.3, 46, 1, 60.9, 90.1, 7.9, 6.73),
(15, '15. Brentford', 'Premier League', 48, 11.7, 40, 1, 48.2, 81.3, 17.3, 6.73),
(16, '16. Lyon', 'Ligue 1', 46, 12.5, 41, 0, 55.7, 85.3, 9.8, 6.73),
(17, '17. Marseille', 'Ligue 1', 52, 14.5, 42, 6, 65, 89.8, 9.5, 6.73),
(18, '18. Tottenham', 'Premier League', 55, 14.3, 52, 1, 57.4, 85.6, 11.3, 6.72),
(19, '19. Eintracht Frankfurt', 'Bundesliga', 51, 14.8, 38, 1, 49, 83.7, 12.7, 6.72),
(20, '20. Nottingham Forest', 'Premier League', 45, 12.5, 59, 2, 39.4, 78.3, 15, 6.72);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `stats_equipes`
--
ALTER TABLE `stats_equipes`
  ADD PRIMARY KEY (`classement`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
