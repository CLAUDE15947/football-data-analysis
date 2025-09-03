-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 14 mars 2025 à 12:49
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
-- Structure de la table `stats_joueurs`
--

CREATE TABLE `stats_joueurs` (
  `id` int(11) NOT NULL,
  `joueur` varchar(255) DEFAULT NULL,
  `equipe` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `poste` varchar(50) DEFAULT NULL,
  `apps` varchar(10) DEFAULT NULL,
  `minutes` int(11) DEFAULT NULL,
  `buts` int(11) DEFAULT NULL,
  `passes` int(11) DEFAULT NULL,
  `jaunes` int(11) DEFAULT NULL,
  `rouges` int(11) DEFAULT NULL,
  `tirs_match` float DEFAULT NULL,
  `passes_pourcent` float DEFAULT NULL,
  `duels_aeriens` float DEFAULT NULL,
  `homme_du_match` int(11) DEFAULT NULL,
  `note` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `stats_joueurs`
--

INSERT INTO `stats_joueurs` (`id`, `joueur`, `equipe`, `age`, `poste`, `apps`, `minutes`, `buts`, `passes`, `jaunes`, `rouges`, `tirs_match`, `passes_pourcent`, `duels_aeriens`, `homme_du_match`, `note`) VALUES
(1, 'Omar Marmoush', 'Eintracht Frankfurt,', 26, ', AM(CL),FW', '17', 1454, 15, 9, 2, 0, 4.5, 79.6, 0.4, 9, 8.23),
(2, 'Lamine Yamal', 'Barcelona,', 17, ', AM(R)', '21(2)', 1885, 5, 11, 2, 0, 3.6, 78, 0, 6, 7.96),
(3, 'Mohamed Salah', 'Liverpool,', 32, ', AM(CLR),FW', '29', 2575, 27, 17, 1, 0, 3.7, 73.6, 0.2, 10, 7.89),
(4, 'Ousmane Dembélé', 'PSG,', 27, ', AM(CLR),FW', '16(7)', 1399, 20, 5, 2, 0, 3.4, 83.7, 0.2, 9, 7.86),
(5, 'Bukayo Saka', 'Arsenal,', 23, ', D(L),M(CLR)', '16', 1276, 5, 10, 3, 0, 2.9, 84.3, 0.5, 6, 7.79),
(6, 'Harry Kane', 'Bayern,', 31, ', AM(C),FW', '21(2)', 1766, 21, 6, 4, 0, 3.7, 81.3, 1, 6, 7.76),
(7, 'Raphinha', 'Barcelona,', 28, ', AM(CLR),FW', '25(1)', 2135, 13, 7, 3, 0, 3.2, 77.9, 0.2, 9, 7.72),
(8, 'Kylian Mbappé', 'Real Madrid,', 26, ', AM(CLR),FW', '25', 2159, 18, 3, 3, 0, 4.4, 85.4, 0.1, 6, 7.64),
(9, 'Florian Wirtz', 'Leverkusen,', 21, ', AM(CLR),FW', '20(5)', 1882, 9, 10, 1, 0, 2.6, 82.7, 0.2, 7, 7.64),
(10, 'Jamal Musiala', 'Bayern,', 22, ', M(CLR)', '18(4)', 1585, 11, 2, 2, 0, 2.7, 83.6, 0.3, 5, 7.62);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `stats_joueurs`
--
ALTER TABLE `stats_joueurs`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
